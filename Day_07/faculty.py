"""

Code Challenge
  Name: 
    Student and Faculty JSON
  Filename: 
    student.json
    faculty.json
  Problem Statement:
    Create a student and Faculty JSON object and get it verified using jsonlint.com
    Write a JSON for faculty profile. 
    The JSON should have profile of minimum 2 faculty members. 
    The profile for each faculty should include below information atleast:

        First Name
        Last Name
        Photo (Just a random url)
        Department 
        Research Areas (can be multiple)
        Contact Details (should include phone number and email id and can have multiple )
   Hint:
       www.jsonlint.com
       
"""

 import json
 
 fact_detail = """
 
{
	"Teachers": {
		"fname": "dhruvin",
		"lname": "panchal",
		"photo": "https://www.google.com/search?q=images&rlz=1C1CHBF_enIN782IN782&source=lnms&tbm=isch&sa=X&ved=0ahUKEwj3tojXopriAhWLvo8KHd4hDLIQ_AUIDigB&biw=1366&bih=608#",
		"Dept": "Computer Science",
		"research_area": ["Toc", "cn"],
		"contact": ["9660090889", " 8888888888", "9999999999"]
	},



	"Teachers1": {
		"fname": "honey",
		"lname": "panchal",
		"photo": "https://www.google.com/imgres?imgurl=https%3A%2F%2Fimages.pexels.com%2Fphotos%2F414612%2Fpexels-photo-414612.jpeg%3Fauto%3Dcompress%26cs%3Dtinysrgb%26dpr%3D1%26w%3D500&imgrefurl=https%3A%2F%2Fwww.pexels.com%2Fsearch%2Fbeauty%2F&docid=pFs_4Fcq5AgpmM&tbnid=aT1lQMo5nzpYfM%3A&vet=10ahUKEwi7xOHeopriAhX_7XMBHXGnBtwQMwhrKAIwAg..i&w=500&h=355&bih=608&biw=1366&q=images&ved=0ahUKEwi7xOHeopriAhX_7XMBHXGnBtwQMwhrKAIwAg&iact=mrc&uact=8",
		"Dept": "Computer Science",
		"research_area": ["Toc", "cn"],

		"contact": ["966009089", "8888888888", "999999999"]
	}
}

"""

stud_details = """

{
	"student": {
		"fname": "dhruvin",
		"lname": "panchal",
		"clg_id": "16egjcs053",
		"photo": "https://www.google.com/search?q=images&rlz=1C1CHBF_enIN782IN782&source=lnms&tbm=isch&sa=X&ved=0ahUKEwj3tojXopriAhWLvo8KHd4hDLIQ_AUIDigB&biw=1366&bih=608#",
		"branch": "Computer Science",
		"research_area": "persuing",
		"contact": ["9660090889", " 8888888888", "9999999999"]
	}
}
    """












