# Technical Specification: Automated Showcase Deck Generator

**Project Name:** Turbo-Flux Showcase Deck Automation  
**Version:** 1.0  
**Date:** 2024  
**Product Manager:** Avinash Agarwal  
**Company:** Cox Automotive

---

## 1. Executive Summary

This document specifies the requirements and technical design for an automated bi-weekly showcase deck generator for the Turbo-Flux team working on the VCA Voice Unified Settings Platform at Cox Automotive. The system will pull data from Rally (CA Agile Central) and generate a professional PowerPoint presentation summarizing sprint accomplishments, KPIs, and team updates.

---

## 2. Project Overview

### 2.1 Purpose
Automate the creation of bi-weekly showcase presentations to reduce manual effort and ensure consistent reporting for stakeholders.

### 2.2 Scope
- Generate PowerPoint presentations on-demand
- Pull sprint data from Rally API
- Accept manual inputs via command-line prompts
- Save presentations to Desktop with standardized naming

### 2.3 Team Information
- **Team Name:** Turbo-Flux
- **Project:** VCA Voice Unified Settings Platform
- **Product Manager:** Avinash Agarwal
- **Team Members:**
  - Kartik (Developer)
  - Vishal (Developer)
  - Ramesh (Developer)
- **Sprint Duration:** 2 weeks

---

## 3. Functional Requirements

### 3.1 Deck Structure
The generated PowerPoint deck will contain exactly **6 slides** in the following order:

#### Slide 1: Project Overview
**Content:**
- Project name: "VCA Voice Unified Settings Platform"
- Team name: "Turbo-Flux"
- Current sprint number (from Rally)
- Sprint dates (start and end date)
- Team member names and roles:
  - Kartik - Developer
  - Vishal - Developer
  - Ramesh - Developer
- Product Manager: Avinash Agarwal
- High-level project status (manual input: On Track / At Risk / Behind)

#### Slide 2: Sprint Progress/Accomplishments
**Content:**
- Sprint identifier (e.g., "Sprint 12")
- List of completed user stories (titles only)
- Number of stories completed
- Number of story points completed

#### Slide 3: Key Performance Indicators (KPIs)
**Content (text-based, bulleted list):**
- Sprint Velocity: [X] story points completed
- Planned vs Actual: [X] planned / [Y] completed story points
- Percentage of Sprint Goal Achieved: [Z]% ([completed stories] / [total planned stories] × 100)

#### Slide 4: Team Updates
**Content (auto-generated from Rally):**
- Summary of completed user stories (titles only)
- Number of stories completed
- Key accomplishments narrative (generated from story titles, descriptions, and completed features)
- Features delivered (list of features completed in the sprint)

#### Slide 5: Blockers/Risks
**Content (manual input):**
- List of current blockers (provided via command-line prompt)
- List of risks (provided via command-line prompt)
- If none, display "No blockers or risks reported"

#### Slide 6: Rally Board Screenshot
**Content:**
- Screenshot image of current Rally board (manually provided by user)
- Image should be inserted and scaled appropriately

### 3.2 Data Sources

#### 3.2.1 Rally (CA Agile Central) API
**Primary data source for:**
- Sprint information (number, dates, status)
- User stories (planned, completed, story points, titles, descriptions)
- Features (completed features in sprint)
- Team velocity and metrics

**Rally Hierarchy:**
- **Epics** → Problem statements
- **Features** → High-level statements of work
- **User Stories** → Deliverable work items

**Completion Criteria:**
- User story status = "Accepted" indicates completion

**Metrics Calculations:**
- **Sprint Velocity:** Sum of story points for all stories with status = "Accepted" in the sprint
- **Planned Story Points:** Sum of all story points for stories planned at sprint start
- **Actual Story Points:** Sum of story points for stories with status = "Accepted"
- **Sprint Goal Percentage:** (Count of accepted stories / Count of planned stories) × 100

#### 3.2.2 Manual Inputs (Command-Line Prompts)
- Project status (On Track / At Risk / Behind)
- Blockers and risks (free text)
- Rally board screenshot file path

### 3.3 Output Specifications

#### 3.3.1 File Format
- **Format:** Microsoft PowerPoint (.pptx)
- **Location:** User's Desktop
- **Naming Convention:** `Turbo-Flux_Showcase_Sprint_<number>.pptx`
  - Example: `Turbo-Flux_Showcase_Sprint_12.pptx`

#### 3.3.2 Design Specifications
- **Styling:** Default professional PowerPoint styling
- **Colors:** Standard corporate color scheme
- **Fonts:** Default system fonts (e.g., Calibri, Arial)
- **Layout:** Clean, consistent formatting across all slides
- **Slide Numbers:** Enabled on all slides
- **Footer:** None
- **PM Name:** "Product Manager: Avinash Agarwal" on title/first slide

### 3.4 User Interaction Flow

1. User executes the script/application manually
2. System prompts for Rally API credentials (if not in .env)
3. System validates Rally connection and retrieves sprint data
4. System prompts user for:
   - Project status (On Track / At Risk / Behind)
   - Blockers (free text, optional)
   - Risks (free text, optional)
   - Rally board screenshot file path
5. System generates PowerPoint presentation
6. System saves file to Desktop
7. System displays console message with file location and success status

---

## 4. Technical Architecture

### 4.1 Technology Stack

**Recommended Stack:**
- **Language:** Python 3.8+
- **Libraries:**
  - `python-pptx` - PowerPoint generation
  - `pyral` or `requests` - Rally API interaction
  - `python-dotenv` - Environment variable management
  - `Pillow` - Image processing for screenshots
  - `argparse` - Command-line argument parsing

**Alternative Stack:**
- Node.js with `pptxgenjs` (if preferred)

### 4.2 System Components

#### 4.2.1 Configuration Manager
- Loads Rally credentials from `.env` file
- Manages project configuration (team members, project name)
- Validates required environment variables

#### 4.2.2 Rally API Client
- Authenticates with Rally API
- Retrieves sprint data (current/most recent completed sprint)
- Queries user stories, features, epics
- Implements retry logic (3 attempts with exponential backoff)
- Validates data completeness before proceeding

#### 4.2.3 Data Processor
- Calculates KPIs (velocity, planned vs actual, sprint goal %)
- Aggregates completed stories and features
- Generates key accomplishments narrative from:
  - Story titles
  - Story descriptions
  - Completed features

#### 4.2.4 User Input Handler
- Prompts for manual inputs via command line
- Validates input formats
- Handles optional inputs (blockers, risks)
- Validates screenshot file path and format

#### 4.2.5 Presentation Generator
- Creates PowerPoint presentation using `python-pptx`
- Applies consistent formatting and styling
- Inserts text content with appropriate formatting
- Embeds Rally board screenshot
- Adds slide numbers
- Saves file to Desktop with correct naming

#### 4.2.6 Error Handler
- Validates Rally API responses
- Implements 3-retry mechanism for API failures
- Logs errors to console
- Provides user-friendly error messages
- Gracefully handles missing or incomplete data

---

## 5. Data Requirements

### 5.1 Environment Variables (.env file)

```
RALLY_API_KEY=<your_rally_api_key>
RALLY_SERVER=https://rally1.rallydev.com
RALLY_WORKSPACE=<workspace_name>
RALLY_PROJECT=<project_name_or_id>
RALLY_USERNAME=<username_optional>
```

### 5.2 Rally API Endpoints Required

- **Workspace/Project Query:** Get project details
- **Iteration Query:** Get current/most recent sprint
- **User Story Query:** Get stories for sprint (filtered by iteration)
- **Feature Query:** Get features associated with completed stories
- **Task Query:** (Optional) Get tasks under stories

### 5.3 Rally Query Filters

- **Sprint Scope:** Most recently completed sprint only
- **Status Filter:** Stories with State = "Accepted"
- **Date Range:** Sprint start date to end date
- **Project Filter:** VCA Voice Unified Settings Platform

---

## 6. Non-Functional Requirements

### 6.1 Performance
- Deck generation should complete within 30 seconds under normal conditions
- Rally API calls should timeout after 10 seconds per request
- Support for sprints with up to 100 user stories

### 6.2 Reliability
- Implement 3-retry mechanism for Rally API failures
- Validate all data before generation
- Handle network interruptions gracefully
- Generate deck even with partial data (with warnings)

### 6.3 Usability
- Clear console messages for each step
- Intuitive command-line prompts
- Helpful error messages with troubleshooting hints
- Confirmation message with file location on success

### 6.4 Security
- Store credentials in `.env` file (not in code)
- `.env` file should be included in `.gitignore`
- No sensitive data in console output
- API key should never be logged

### 6.5 Maintainability
- Modular code architecture
- Well-documented functions and classes
- Configuration separated from code
- Easy to update slide templates

---

## 7. User Stories

### 7.1 As a Product Manager
**Story 1:** Generate Showcase Deck on Demand
- **Given** I have Rally credentials configured
- **When** I run the deck generator script
- **Then** I should be prompted for manual inputs and receive a PowerPoint file on my Desktop

**Story 2:** View Sprint Metrics
- **Given** The deck is generated
- **When** I open the PowerPoint file
- **Then** I should see accurate KPIs for the most recently completed sprint

**Story 3:** Include Manual Context
- **Given** I need to add blockers or risks
- **When** I'm prompted during generation
- **Then** I can input text that appears in the Blockers/Risks slide

**Story 4:** Regenerate/Update Deck
- **Given** I've generated a deck but need to update it
- **When** I run the script again with the same sprint
- **Then** The system should regenerate/overwrite the deck with updated data

### 7.2 As a Developer (Future Enhancement)
**Story 5:** Automated Scheduling (Future)
- **Given** I want to automate the process
- **When** I configure a schedule
- **Then** The deck should be generated automatically every 2 weeks

---

## 8. Error Handling Scenarios

### 8.1 Rally API Errors
| Error Condition | System Response |
|----------------|-----------------|
| Authentication failure | Retry 3 times, then display error: "Rally authentication failed. Check API key in .env file" |
| Network timeout | Retry 3 times with exponential backoff, then display error: "Unable to connect to Rally. Check network connection" |
| Sprint not found | Display error: "No completed sprint found. Verify sprint exists in Rally" |
| No stories in sprint | Display warning, generate deck with "No stories completed" message |
| Incomplete data | Display warning, generate deck with available data and note missing information |

### 8.2 User Input Errors
| Error Condition | System Response |
|----------------|-----------------|
| Invalid screenshot path | Re-prompt user with error: "File not found. Please enter valid screenshot path" |
| Invalid image format | Re-prompt: "Unsupported format. Please provide PNG, JPG, or BMP file" |
| Missing required input | Re-prompt: "This field is required. Please enter a value" |

### 8.3 File System Errors
| Error Condition | System Response |
|----------------|-----------------|
| Desktop not accessible | Display error: "Cannot access Desktop. Check permissions" |
| Disk full | Display error: "Insufficient disk space to save presentation" |
| File already open | Display error: "Close existing file and try again, or rename manually" |

---

## 9. Implementation Phases

### Phase 1: Core Functionality (MVP)
**Deliverables:**
- Rally API integration
- Data retrieval and KPI calculation
- Basic PowerPoint generation (6 slides)
- Command-line interface
- Manual trigger execution

**Timeline:** 2-3 weeks

### Phase 2: Enhancement & Polish
**Deliverables:**
- Improved error handling
- Better narrative generation for accomplishments
- Enhanced slide formatting
- Comprehensive testing

**Timeline:** 1 week

### Phase 3: Future Enhancements (Optional)
**Potential Features:**
- Automated scheduling (cron job / Task Scheduler)
- Email delivery of generated deck
- Historical trend charts (velocity over time)
- Custom slide templates
- Web-based UI instead of CLI
- Export to multiple formats (PDF, Google Slides)

---

## 10. Testing Requirements

### 10.1 Unit Tests
- Rally API client functions
- KPI calculation logic
- Data aggregation functions
- File naming logic

### 10.2 Integration Tests
- End-to-end deck generation
- Rally API connectivity
- File system operations
- Error handling scenarios

### 10.3 User Acceptance Testing
- Generate deck with real sprint data
- Verify all metrics are accurate
- Validate slide content and formatting
- Test with various sprint scenarios (incomplete sprints, no stories, etc.)

---

## 11. Deployment & Usage

### 11.1 Installation Steps
1. Clone repository
2. Install Python 3.8+ (if not installed)
3. Install dependencies: `pip install -r requirements.txt`
4. Create `.env` file with Rally credentials
5. Configure team/project details (if not hardcoded)

### 11.2 Execution
```bash
python generate_showcase_deck.py
```

### 11.3 Expected Output
```
=== Turbo-Flux Showcase Deck Generator ===

Connecting to Rally...
✓ Rally connection successful

Retrieving sprint data...
✓ Found Sprint 12 (01/15/2024 - 01/28/2024)
✓ Retrieved 15 user stories (12 accepted)

Enter project status (On Track/At Risk/Behind): On Track
Enter blockers (or press Enter to skip): 
Enter risks (or press Enter to skip): API rate limiting concerns
Enter path to Rally board screenshot: C:\Users\Avinash\Desktop\rally_board.png
✓ Screenshot loaded

Generating presentation...
✓ Slide 1: Project Overview
✓ Slide 2: Sprint Progress
✓ Slide 3: KPIs
✓ Slide 4: Team Updates
✓ Slide 5: Blockers/Risks
✓ Slide 6: Rally Board Screenshot

Saving to Desktop...
✓ SUCCESS: Turbo-Flux_Showcase_Sprint_12.pptx saved to Desktop

Deck generation complete!
```

---

## 12. Maintenance & Support

### 12.1 Regular Maintenance
- Update Rally API client if Rally changes their API
- Refresh dependencies quarterly
- Review and update KPI calculations as needed

### 12.2 Documentation
- Maintain README with setup instructions
- Document Rally API queries and filters
- Keep architecture diagrams updated

### 12.3 Support Contacts
- Technical Issues: Development team
- Rally Access: Cox Automotive IT
- Business Requirements: Avinash Agarwal (PM)

---

## 13. Risks & Mitigation

| Risk | Impact | Likelihood | Mitigation |
|------|--------|------------|------------|
| Rally API changes | High | Medium | Use official SDK, implement version checking |
| API rate limiting | Medium | Low | Implement caching, optimize queries |
| Incomplete sprint data | Medium | Medium | Validate data, provide clear warnings |
| Screenshot quality issues | Low | Medium | Accept multiple formats, provide resize options |
| Credential exposure | High | Low | Use .env file, add to .gitignore, educate users |

---

## 14. Success Criteria

The project will be considered successful when:
- ✅ Deck generation completes in < 30 seconds
- ✅ All 6 slides contain accurate, well-formatted data
- ✅ Rally data is correctly retrieved and calculated
- ✅ Manual inputs are seamlessly integrated
- ✅ Error handling provides clear, actionable messages
- ✅ File is saved to Desktop with correct naming
- ✅ PM can generate deck without technical assistance
- ✅ Deck is presentation-ready (minimal manual editing needed)

---

## 15. Glossary

| Term | Definition |
|------|------------|
| Rally | CA Agile Central - Agile project management platform |
| Sprint | 2-week development iteration |
| Story Points | Unit of effort estimation for user stories |
| Velocity | Total story points completed in a sprint |
| Epic | High-level problem statement in Rally hierarchy |
| Feature | Mid-level work statement, child of Epic |
| User Story | Granular deliverable work item, child of Feature |
| Accepted | Rally status indicating story completion |
| VCA | Voice unified settings platform (project name) |
| Turbo-Flux | Team name |

---

## 16. Appendices

### Appendix A: Sample .env File
```env
# Rally API Configuration
RALLY_API_KEY=_your_api_key_here_
RALLY_SERVER=https://rally1.rallydev.com
RALLY_WORKSPACE=Cox Automotive
RALLY_PROJECT=VCA Voice Unified Settings Platform
```

### Appendix B: Sample Command-Line Interaction
```
$ python generate_showcase_deck.py

=== Turbo-Flux Showcase Deck Generator ===

Connecting to Rally... ✓
Retrieving Sprint 12 data... ✓

Please provide the following information:

1. Project Status (On Track/At Risk/Behind): On Track
2. Blockers (press Enter if none): 
3. Risks (press Enter if none): 
4. Rally Board Screenshot Path: C:\Users\Avinash\Desktop\board.png

Generating deck... ✓
Saved: C:\Users\Avinash\Desktop\Turbo-Flux_Showcase_Sprint_12.pptx

Generation complete!
```

### Appendix C: Rally API Query Examples
```python
# Example: Get most recent completed sprint
iteration_query = f'(Project.Name = "VCA Voice Unified Settings Platform") AND (EndDate <= today) AND (StartDate >= today-30)'

# Example: Get accepted stories in sprint
story_query = f'(Iteration.Name = "Sprint 12") AND (ScheduleState = "Accepted")'
```

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2024 | CodeMie Developer | Initial specification based on PM interview |

---

**End of Specification Document**
