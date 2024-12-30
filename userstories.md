# User Stories

## User Story 1: Select Nutritionist

**As a** client user,
**I want** to view a list of available nutritionists,
**So that** I can choose a nutritionist for my consultations.

### Acceptance Criteria
- The user must be authenticated as a client.
- The user should see a list of nutritionists with basic information, such as name, email, and registration number.
- The user should be able to select a nutritionist from the list.
- The selected nutritionist should be saved in the client's profile.

---

## User Story 2: Client Registration

**As an** administrator,
**I want** to register new clients in the system,
**So that** they can access the services offered by the platform.

### Acceptance Criteria
- The administrator should fill out a form with basic client information, such as name, email, phone, and password.
- The system should validate the information and create a client profile.

## User Story 3: Register as a Nutritionist
**As a** nutritionist,
**I want** to register with my professional details,
**So that** I can manage my clients and appointments effectively through the platform.

### Acceptance Criteria:

- Nutritionists must provide their name, email, registration number, and phone number during registration.
- The system should validate the registration number for uniqueness.
- If any required field is missing or invalid, the system should display an appropriate error message.

## User Story 4: View My Clients
**As a** nutritionist,
**I want** to view a list of my registered clients,
**So that** I can easily access their health information and track their progress.

### Acceptance Criteria:

- The dashboard should display a list of clients linked to the logged-in nutritionist.
- Each client entry should include the client’s name, contact information, and a summary of their health data.
- If no clients are registered, the system should display a message indicating no clients are available.