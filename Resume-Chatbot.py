
import google.generativeai as genai
import os
from datetime import datetime

# Configure Gemini API
API_KEY = "AIzaSyCXB-N3Rw52PjcRPED-o5Sbw_NhNEgJ3HA"  # Your provided API key
genai.configure(api_key=API_KEY)

# Create Gemini model - Updated to use Gemini 2.5 Pro
model = genai.GenerativeModel("gemini-2.5-pro")  # Using Gemini 2.5 Pro


# Function to take user input for resume
def get_user_details():
    print("=" * 50)
    print("🎯 Welcome to AI Resume Builder Chatbot!")
    print("=" * 50)
    print("Please enter the following details:\n")

    name = input("📝 Full Name: ")
    email = input("📧 Email: ")
    phone = input("📱 Phone Number: ")
    linkedin = input("🔗 LinkedIn URL (optional): ")
    website = input("🌐 Portfolio/Website (optional): ")
    location = input("📍 Location (City, State): ")

    print("\n--- Professional Information ---")
    summary = input("💼 Professional Summary (2-3 lines): ")
    skills = input("🛠️  Skills (comma-separated): ")

    print("\n--- Education ---")
    education = input("🎓 Education (Degree, Institute, Year): ")

    print("\n--- Work Experience ---")
    experience = input("💼 Work Experience (Role | Company | Duration | Key achievements): ")

    print("\n--- Projects ---")
    projects = input("🚀 Projects (Name | Description | Technologies used): ")

    print("\n--- Additional Information ---")
    certifications = input("🏆 Certifications (optional): ")
    languages = input("🗣️  Languages (optional): ")

    return {
        "name": name,
        "email": email,
        "phone": phone,
        "linkedin": linkedin,
        "website": website,
        "location": location,
        "summary": summary,
        "skills": skills,
        "education": education,
        "experience": experience,
        "projects": projects,
        "certifications": certifications,
        "languages": languages
    }


# Function to generate resume using Gemini
def generate_resume(details):
    prompt = f"""
Create a professional, modern resume in clean text format using the following details:

PERSONAL INFORMATION:
- Full Name: {details['name']}
- Email: {details['email']}
- Phone: {details['phone']}
- LinkedIn: {details['linkedin']}
- Website: {details['website']}
- Location: {details['location']}

CONTENT:
- Professional Summary: {details['summary']}
- Skills: {details['skills']}
- Education: {details['education']}
- Experience: {details['experience']}
- Projects: {details['projects']}
- Certifications: {details['certifications']}
- Languages: {details['languages']}

FORMATTING REQUIREMENTS:
1. Use a clean, professional layout with clear section headers
2. Include proper spacing and alignment
3. Use bullet points for achievements and responsibilities
4. Make it ATS-friendly (Applicant Tracking System)
5. Ensure the content is concise but impactful
6. Use action verbs for experience descriptions
7. Include quantifiable achievements where possible

Please create a complete, professional resume that would impress recruiters and hiring managers.
    """

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error generating resume: {str(e)}"


# Function to save resume with timestamp
def save_resume(resume_text, name):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"resume_{name.replace(' ', '_')}_{timestamp}.txt"

    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(resume_text)
        return filename
    except Exception as e:
        return f"Error saving file: {str(e)}"


# Function to preview resume sections
def preview_details(details):
    print("\n" + "=" * 50)
    print("📋 RESUME PREVIEW")
    print("=" * 50)

    for key, value in details.items():
        if value.strip():  # Only show non-empty fields
            print(f"{key.capitalize()}: {value}")

    print("=" * 50)
    confirm = input("\n✅ Does this information look correct? (yes/no): ").strip().lower()
    return confirm == "yes"


# Enhanced main function
def main():
    print("🤖 AI-Powered Resume Builder")
    print("Using Google Gemini 2.5 Pro for intelligent resume generation\n")

    while True:
        try:
            # Get user details
            user_details = get_user_details()

            # Preview and confirm details
            if not preview_details(user_details):
                retry = input("Would you like to re-enter your information? (yes/no): ").strip().lower()
                if retry != "yes":
                    break
                continue

            # Generate resume
            print("\n🔄 Generating your professional resume... Please wait.\n")
            resume_text = generate_resume(user_details)

            if resume_text.startswith("Error"):
                print(f"❌ {resume_text}")
                break

            # Display resume
            print("=" * 60)
            print("📄 YOUR GENERATED RESUME")
            print("=" * 60)
            print(resume_text)
            print("=" * 60)

            # Save options
            save_option = input("\n💾 Do you want to save the resume to a file? (yes/no): ").strip().lower()
            if save_option == "yes":
                filename = save_resume(resume_text, user_details['name'])
                if filename.startswith("Error"):
                    print(f"❌ {filename}")
                else:
                    print(f"✅ Resume saved as '{filename}'")

            # Ask for another resume
            another = input("\n🔄 Would you like to create another resume? (yes/no): ").strip().lower()
            if another != "yes":
                break

        except KeyboardInterrupt:
            print("\n\n👋 Thank you for using AI Resume Builder!")
            break
        except Exception as e:
            print(f"\n❌ An unexpected error occurred: {str(e)}")
            break

    print("\n🎉 Thank you for using AI Resume Builder! Good luck with your job search!")


# Fixed the syntax error in the original code
if __name__ == "__main__":
    main()
