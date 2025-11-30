from app.services.ai_analyzer import ai_analyzer
from app.services.github_validator import github_validator
import json

def test_manual_data():
    print("Running Manual Test with User Data...\n")

    # 1. Setup Data
    candidate_data = {
        "id": "7",
        "name": "Akilan Kumar S",
        "email": "akilan6793eee@gmail.com",
        "github_url": "https://github.com/akilan6793eee/",
        "resume_text": """
Akilan Kumar S 
Embedded Engineer 
 
No: 3F Emerald Olympia 
opaline Chennai – 600 130 
+91 - 9677322511 
akilan6793eee@gmail.com 
 
CAREER OBJECTIVE 
Scaling new heights of success and leaving a mark of excellence in every assignment which involves 
analytical capabilities and professional growth. 
 
EXPERIENCE 
 
Totally 7.5 + years of experience  
 
Having 1.4 years of experience in Automotive domain in Car audio  
at Tata Elxsi Pvt Ltd Chennai- Specialist from January -2024 to present  
 
Having 6.4 years of experience in Embedded Software 
Development Jasmin-Infotech Pvt Ltd, Chennai – Senior 
Systems Engineer December 2022  
 
EDUCATION 
Pavendar Bharathidasan College of Engineering and Technology, Trichy - B.E - 2015 
Electronics and Communication Engineering, 7.07 CGPA 
Shanmuga Polytechnic College, Thanjavur – Diploma - 2012 
State board, 77.9% 
Allwin Higher Secondary School, Thanjavur – SSLC - 2009 
State board, 71.2% 
 
AREA OF EXPERTISE 
Automotive car audio, Audio Signal Processing, DSP processors, Cross compilation, MIPS and 
Memory optimizations, JTAG Debugging, Communication protocols like UART, SPI. 
 
TOOLS WORKED 
GTT, JIRA, Mentor analyzer, Source tree, APX, MP Bios Control, IAR, Citrix Receiver Jlink 
Debugger ,Visual code, Microsoft Visual Studio, Cross Core Embedded Studio, Audacity, Spectra lab, 
beyond compare, Element tool. 
HARDWARE PLATFORMS WORKED 
SHARC Processor: ADSP 21593 W, ADSP – 21489, ADSP – 21573, ADSP – 21569,  SC-589, SC-573 
 
 
 
AREA OF EXPERTISE 
❖ Experience in Honda Acura Car audio system.  
❖ Implementation of HBBIOS software for board bring up in Honda project.  
❖ Audio Signal Processing in DSP processors such as SHARC+ ( JTAG & JLinker Debugging and 
flashing). 
❖ Experience in porting and integrating Virtual X  DTSX libraries in DSP. 
❖ Experience in Communication protocols like UART, SPI, I2S and TDM. 
❖ Good exposure to code and memory optimization techniques for embedded solutions. 
❖ Design Development, Cross Compilation, and Library Integration. 
❖ Porting libraries in SHARC processors - MIPS, and Memory optimization. 
❖ Experience in analysis, coding, debugging, unit and functional testing of the modules. 
❖ Post-processing technology in Virtual X and DTSX Libraries. 
 
SKILLS 
 
❖ Hand on expertise in APX 
❖ The build system created for the Honda project is based on variant specific project.  
❖ Implementation of HBBIOS software for board bring up in Honda project.  
❖ Hand on expertise in GTT 
❖ Platform PDK Integration in Honda project 
❖ Design, develop, code, test and debug embedded software solutions for a variety of platforms. 
❖ Operating Systems: Windows XP/7,10,11 Linux 
❖ Working knowledge of C, and assembly language 
❖ Working in A2B Mentor Analyzer for sending the external clock to the  project, creating the session file 
based on project.  
❖ Cross compilation, MIPS and Memory Optimizations, Review code and design. 
❖ Compiler level optimization for reducing MIPS. 
❖ Real time audio framework design and development in SHARC processors. 
❖ Work effectively in a team of engineers, both learning from and mentoring others. 
❖ Work with Digite, SVN, and GIT for project management and project version control. 
❖ Significant experience of working with customers, project managers and technical teams for securing & 
 
 
executing concurrent projects 
CERTIFICATION 
Completed Certified Advanced Course in Embedded Systems from Vector Institution 
 
Projects 
 
Title: Honda Acura 3MAA project 
Platform: ADSP-21593 
Tools: CCES 2.11.1 
Contribution: Pdk platform code integration on Honda project, Extendable Audio framework integration and 
Implementation of  Features as per the requirements, Features such as (ANC, Feedback, QLS, Fader balance 
,volume and mute block, gain control, Dolby) Debugging and resolving customer reported issues and Bug 
fixing, Initially Board bring up  for the project,  
Title: DTS VirtualX ON Griffin Lite XP Processor 
 
Platform: ADSP-21593 
Tools: CCES 2.10.0 
 
Contribution:  Porting of VirtualX in GLXP Processor, Cross compiling in CCES environment, removing 
dynamic memory allocations by static buffers, Code modified to support CAT evaluation, Debugging and 
resolving issues, Test Plan preparation and unit testing and Optimization, Real-time kernel design and 
implementation, Real time  decoders DTS VirtualX decoder cross compilation, MIPS split up and 
Optimization of the code for targeted MIPS and memory. Also helped with customer query support. 
 
Title: CES_DEMO_Gaming_Speaker 
Platform: ADSP-21569 
Tools: CCES 2.9.1 
Contribution: Real-time kernel design and implementation, Real time  decoders like  Dolby  Digital 
decoder cross compilation, Headphone-x and stereoplus porting and cross compilation, Debugging and 
resolving customer reported issues, MIPS split up. UART configuration For GUI Support. 
Title: DTS VirtualX ON Griffin Lite XP Processor 
 
Platform: ADSP-21593 
Tools: CCES 2.10.0 
 
Contribution:  Porting of VirtualX in GLXP Processor, Cross compiling in CCES environment, removing 
dynamic memory allocations by static buffers, Code modified to support CAT evaluation, Debugging and 
resolving issues, Test Plan preparation and unit testing, MIPS split up and Optimization, Data match 
analysis for all the supported streams. Real-time kernel design and implementation, Real time  decoders 
DTS VirtualX decoder cross compilation, MIPS split up and Optimization of the code for targeted MIPS 
and memory. Also helped with customer query support. 
 
 
 
 
 
Title: DTS VirtualX Porting ON GRIFFIN ULTRALITE Processor 
 
Platform: ADSP-21569 
Tools: CCES 2.9.0 & CCES 2.9.1 
Contribution: Porting of VirtualX in Griffin Ultra lite Processor, Cross compiling in CCES environment, 
removing dynamic memory allocations by static buffers, Code modified to support CAT evaluation, 
Debugging and resolving issues, Test Plan preparation and unit testing, MIPS split up and Optimization, 
Data match analysis for all the supported streams. 
Title: DTSX Porting ON GRIFFINLITE Processor 
 
Platform: ADSP-21573 
Tools: CCES 2.6.0 
 
Contribution: Cross compiling in CCES environment, removing dynamic memory allocations by static 
buffers, Code modified to support CAT evaluation, Debugging and resolving issues, Test Plan preparation 
and unit testing, MIPS split up and Optimization, Data match analysis for all the supported streams. 
 
Title: DTSX Porting ON GRIFFIN 
Platform: ADSP-21589 
Tools: CCES 2.2.0 
 
Contribution:  Porting of DTSX libraries, Memory usage Calculation, Code modified to support USB 
input/output, CAT evaluation for all cases, Debugging and resolving issues, Test Plan preparation and unit 
testing, MIPS split up and Optimization. 
 
PERSONAL DETAILS 
Father’s Name : Mr. KS Shanmugasundaram 
Date of Birth : 06-07-1993 
Gender : Male 
Nationality : Indian 
Languages : Tamil, English, Hindi (Speak only) 
Hobbies : Playing Sudoku, Cricket 
Marital Status : Married 
 
 
DECLARATION 
I hereby declare that all the details furnished above are true to the best of my knowledge. 
 
 
Place: (CHENNAI)           
Date : 
"""
    }

    job_description = "RICEF, RAP. experience : 4"

    # 2. Run AI Analysis (Evaluation)
    print("--- AI Analysis (Evaluation) ---")
    try:
        report = ai_analyzer.analyze_candidate(candidate_data, job_description)
        print(json.dumps(report, indent=2))
    except Exception as e:
        print(f"Error in AI Analysis: {e}")

    # 3. Run GitHub Deep Check
    print("\n--- GitHub Deep Validation ---")
    try:
        validation = github_validator.validate_github_profile(candidate_data['github_url'])
        print(json.dumps(validation, indent=2))
    except Exception as e:
        print(f"Error in GitHub Validation: {e}")

if __name__ == "__main__":
    test_manual_data()
