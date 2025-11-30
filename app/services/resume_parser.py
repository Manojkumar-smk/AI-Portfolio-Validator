from pypdf import PdfReader
import io

class ResumeParser:
    def extract_text(self, file_stream):
        """
        Extracts text from a resume file stream (PDF).
        """
        try:
            reader = PdfReader(file_stream)
            text = ""
            for page in reader.pages:
                text += page.extract_text() + "\n"
            return text
        except Exception as e:
            print(f"Error reading PDF: {e}")
            return ""

    def parse_details(self, text):
        """
        Extracts structured details like Email, LinkedIn, GitHub from text.
        """
        # Simple extraction logic for demonstration
        import re
        
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        github_pattern = r'github\.com\/([a-zA-Z0-9-]+)'
        linkedin_pattern = r'linkedin\.com\/in\/([a-zA-Z0-9-]+)'
        
        email = re.search(email_pattern, text)
        github = re.search(github_pattern, text)
        linkedin = re.search(linkedin_pattern, text)
        
        return {
            "email": email.group(0) if email else None,
            "github": f"https://github.com/{github.group(1)}" if github else None,
            "linkedin": f"https://linkedin.com/in/{linkedin.group(1)}" if linkedin else None,
            "skills": [] # TODO: Add skill extraction logic
        }

resume_parser = ResumeParser()
