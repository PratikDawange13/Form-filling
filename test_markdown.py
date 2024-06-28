from markdown_pdf import MarkdownPdf, Section

markdown_content = """
Filled Form Details
## Person 1 Information:

**Personal Information**

* **Full Name (as per passport):** Vishal Prakash Pawar
* **Phone Number:** +2348097903450
* **Email Address:** kashpawar87@gmail.com
* **Maiden Name:** Nil
* **Marital Status:** Married
* **Place of Birth:** Ichhapur Burhanpur, Madhya Pra, India 
* **Residential Address:** Federal housing complex (1004 Estate),Flat 718, Block D1 Victoria Island Lagos Nigeria.
* **Mailing Address:** Same as residential address
* **Length of Residence:** 1 year
* **Home Ownership:** Renting
* **Other Nationality:** No
* **Tribe:** India, Hindu
* **Languages Spoken:**  (Not specified)

**Spouse Information**

* **Date of Birth:** 2 January 1992
* **Place of Birth:** India
* **Nationality:** India
* **Phone Number:** Nil
* **Email Address:** Nil

**UK Visa Information**

* **Previous UK Visa Applications:** Yes, September 2015
* **Previous UK Visa Issuance:** Yes
* **Previous UK Visa Denial:** No
* **Previous UK Visit:** 
    * Date of Arrival: September 2015
    * Date of Departure: Nil
* **Refused Entry to UK:** No
* **Passport Stolen:** No
* **Intended Date of Arrival to UK:** 17 October 2022
* **Intended City/State of Destination:** Whites Foodservice Equipment Ltd
* **Intended Length of Stay:** 1 week
* **Reason for Travel:** Business-related training
* **Trip Sponsor:** Self
* **Traveling with Others:** No
* **Immigrant Petition Filed:** No

**Other Countries Visa Information**

* **Previous Visa Denial:** No

**Contact Person in UK**

* **Name:** Tim White
* **Address:** Unit 8, Padgets Lane,South Moons Moat, Redditch B98 0RA
* **Phone Number:** 1527528841

**Family Information**

* **Father:** 
    * **Name:** Prakash Pawar
    * **Residential Address:** Nil
    * **Phone Number:** Nil
    * **Place of Birth:** Nil
    * **Date of Birth:** 11 June 1956
* **Mother:**
    * **Name:** Nita Prakash Pawar
    * **Residential Address:** Nil
    * **Phone Number:** Nil
    * **Place of Birth:** Nil
    * **Date of Birth:** 1 June 1957
* **Father or Mother in UK:** No
* **Children:**
    * **Name:** Manvi Pawar
    * **Residential Address:** Federal housing complex (1004 Estate),Flat 718, Block D1 Victoria Island Lagos Nigeria 
    * **Phone Number:** Nil
    * **Place of Birth:** Nigeria
    * **Passport Number:** Nil
* **Immediate Relatives in UK:** No
* **Other Relatives in UK:** No

**Employment Information**

* **Occupation:** Head of Maintenance
* **Organization:** Eat N Go LTD
* **Work Address:** 1715 Idejo Street, Victoria Island Lagos Nigeria
* **Start Date of Employment:** January 2015
* **Employer's Phone Number:** +234 8135343181
* **Name of Supervisor:** Nil
* **Monthly Salary:** 2484000.00 NGN
* **Job Duties:** 
    * Handling 20 technicians and 5 area supervisors 
    * Monitoring tasks
    * Weekly updates on causes and resolution
    * Maintaining inventory costs within budget
    * Submitting checklists and schedules

* **Previous Employment:** Nil
* **Employment in last 5 Years:** Nil
* **Armed Forces, Government, Judiciary, Media, Public or Civil Administration Employment:** No
* **Charitable Organization Involvement:** No

**Travel History**

* **Travel in last 5 Years:** Yes
    * **Country:** India
    * **Period Traveled:** 2 November 2021 - 3 December 2021
    * **Reason:** Tourism

**Education Information**

* **Academic Qualifications:** Nil
"""


pdf = MarkdownPdf()
pdf.add_section(Section(markdown_content, toc=False))
pdf.save('output2.pdf')