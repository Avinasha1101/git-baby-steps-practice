#!/usr/bin/env python3
"""
Markdown File AI Processor

Processes all markdown files in the work/ directory using Claude AI (Anthropic API).
Generates summaries and saves them to work/bulk-processing/output/

Requirements:
    pip install anthropic python-dotenv

Usage:
    python process_markdown_ai.py
"""

import os
import sys
from pathlib import Path
from dotenv import load_dotenv
from anthropic import Anthropic

# Load environment variables from .env file
# Look for .env in the project root (module03-task directory)
script_dir = Path(__file__).resolve().parent  # Module 15
project_root = script_dir.parent  # module03-task
work_root = project_root.parent  # work directory
env_path = project_root / ".env"
load_dotenv(dotenv_path=env_path)

# Get API key from environment
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

if not ANTHROPIC_API_KEY:
    print(f"Error: ANTHROPIC_API_KEY not found in .env file")
    print(f"Looking for .env at: {env_path}")
    print("Please ensure .env file exists with: ANTHROPIC_API_KEY=your_key_here")
    sys.exit(1)

# Initialize Anthropic client
client = Anthropic(api_key=ANTHROPIC_API_KEY)

# Configuration
WORK_DIR = work_root  # Points to C:\Workspace\hello-genAI\work
OUTPUT_DIR = WORK_DIR / "bulk-processing" / "output"
MODEL = "claude-3-opus-20240229"  # Claude 3 Opus - most capable model


def find_markdown_files(directory):
    """Find all markdown files in the specified directory."""
    md_files = []
    work_path = Path(directory)
    
    if not work_path.exists():
        print(f"Error: Directory not found: {directory}")
        return md_files
    
    # Find all .md files (non-recursive for now)
    for file_path in work_path.glob("*.md"):
        if file_path.is_file():
            md_files.append(file_path)
    
    return md_files


def summarize_with_claude(content, filename):
    """Send content to Claude API for summarization."""
    try:
        prompt = f"""Please provide a concise summary of the following markdown document.

Document name: {filename}

Content:
{content}

Provide a clear, structured summary that captures:
1. Main purpose/topic
2. Key points or sections
3. Important details or metrics (if any)
4. Overall conclusions

Keep the summary professional and concise."""

        message = client.messages.create(
            model=MODEL,
            max_tokens=1024,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        
        return message.content[0].text
    
    except Exception as e:
        return f"Error processing with Claude API: {str(e)}"


def process_markdown_files():
    """Main processing function."""
    print("Starting markdown processing...")
    print(f"Script location: {Path(__file__).resolve()}")
    print(f"Project root (module03-task): {project_root}")
    print(f"Work directory: {WORK_DIR}")
    
    # Find all markdown files
    md_files = find_markdown_files(WORK_DIR)
    
    if not md_files:
        print(f"\nNo markdown files found in {WORK_DIR}")
        return
    
    print(f"Found {len(md_files)} markdown files in work/\n")
    
    # Create output directory if it doesn't exist
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    print(f"Output directory: {OUTPUT_DIR}\n")
    
    # Process each file
    processed_count = 0
    error_count = 0
    
    for md_file in md_files:
        try:
            print(f"Processing: {md_file.name}")
            
            # Read the markdown file
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Get summary from Claude
            summary = summarize_with_claude(content, md_file.name)
            
            # Generate output filename
            output_filename = f"{md_file.stem}_report.txt"
            output_path = OUTPUT_DIR / output_filename
            
            # Save summary
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(f"Summary Report for: {md_file.name}\n")
                f.write("=" * 80 + "\n\n")
                f.write(summary)
                f.write("\n\n" + "=" * 80 + "\n")
                f.write(f"Generated using Claude AI ({MODEL})\n")
            
            print(f"[OK] Saved summary to: work/bulk-processing/output/{output_filename}\n")
            processed_count += 1

        except Exception as e:
            print(f"[ERROR] Error processing {md_file.name}: {str(e)}\n")
            error_count += 1
    
    # Summary
    print("-" * 80)
    print(f"Processing complete!")
    print(f"Successfully processed: {processed_count} files")
    if error_count > 0:
        print(f"Errors encountered: {error_count} files")
    print(f"Output saved to: work/bulk-processing/output/")


if __name__ == "__main__":
    try:
        process_markdown_files()
    except KeyboardInterrupt:
        print("\n\nProcessing interrupted by user.")
        sys.exit(0)
    except Exception as e:
        print(f"\n\nFatal error: {str(e)}")
        sys.exit(1)
