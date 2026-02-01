---
agent: agent
description: Create a new programming homework assignment that matches the project structure
argument-hint: Provide assignment details
---

# Create New Programming Assignment

Your goal is to generate a new homework assignment for the Mergington High School students that matches the existing project structure.
To test this prompt, open Copilot Chat in Agent mode and run the following command:

/new-assignment

or

/new-assignment Building REST APIs with FastAPI framework
## Step 1: Gather Assignment Information
If not already provided by the user, ask what the assignment will be about and ensure it aligns with the existing curriculum.

## Step 2: Create Assignment Structure
1. Create a new directory in the `assignments` folder with a unique name based on the assignment topic
2. Create a new file in the directory named `README.md` with the structure from the [assignment-template.md](../../templates/assignment-template.md)
3. Fill out the assignment details in the README file
4. (Optional) Add starter code or attachments if the assignment needs them

## Step 3: Update Website Configuration
Update the assignments list in [config.json](../../config.json) file to include the new assignment.  
For `dueDate`, use current date + 7 days unless specified.

