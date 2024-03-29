import streamlit as st

def main():
    st.set_page_config(page_title="Ta Da Portfolio", page_icon="✨")

    # Create a box for the title
    st.markdown(
        """
        <div style='background-color: rgba(52, 152, 219, 0.3); padding: 20px; border-radius: 10px;'>
            <h1 style='color: white; text-align: center;'>Ta Da Portfolio</h1>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Navigation Bar
    st.markdown("""
        <style>
            .navbar {
                overflow: hidden;
                background-color: #2c3e50;
            }

            .navbar a {
                float: left;
                display: block;
                color: #ecf0f1;
                text-align: center;
                padding: 14px 16px;
                text-decoration: none;
            }

            .navbar a:hover {
                background-color: #34495e;
                color: #ecf0f1;
            }
        </style>
    """, unsafe_allow_html=True)

    # Navigation Bar
    st.markdown("""
        <style>
            .navbar {
                overflow: hidden;
                background-color: #2c3e50;
            }

            .navbar a {
                float: left;
                display: block;
                color: #ecf0f1;
                text-align: center;
                padding: 14px 16px;
                text-decoration: none;
            }

            .navbar a:hover {
                background-color: #34495e;
                color: #ecf0f1;
            }

            /* Highlight the current page */
            .navbar a.active {
                background-color: #34495e;
            }
        </style>
    """, unsafe_allow_html=True)

    # Apply custom styles to the sidebar radio buttons
    st.markdown(
        """
        <style>
            .sidebar .css-17cn3wg {
                list-style-type: none;
                padding: 10px;
                margin-bottom: 10px;
                border-radius: 5px;
                cursor: pointer;
                background-color: #3498db;
                color: white;
            }
            .sidebar .css-17cn3wg:hover {
                background-color: #2980b9;
            }

            .education-details {
            margin-bottom: 20px;
            }

            .education-item {
                font-weight: bold;
                margin-bottom: 5px;
            }
        </style>

        
        """,
        unsafe_allow_html=True,
    )


    # Initial state
    current_page = "About Me"

    # Create sidebar radio buttons
    st.sidebar.title("Navigation")
    about_me_button = st.sidebar.button("About Me")
    experience_button = st.sidebar.button("Experience")
    community_button = st.sidebar.button("Community")
    contact_me_button = st.sidebar.button("Contact Me")
    # Create sidebar radio buttons
    st.sidebar.caption('Wish to connect?')
    st.sidebar.write('📧: tadahray77@gmail.com')
    pdfFileObj = open('Ta-Da-Resume.pdf', 'rb')
    st.sidebar.download_button('Click to Download Resume',pdfFileObj,file_name='Ta-Da-Resume.pdf',mime='pdf')
    
    if about_me_button:
        current_page = "About Me"
    elif experience_button:
        current_page = "Experience"
    elif community_button:
        current_page = "Community"
    elif contact_me_button:
        current_page = "Contact Me"

    # Display content based on the selected page
    if current_page == "About Me":
        about_me()
    elif current_page == "Experience":
        experience()
    elif current_page == "Community":
        community()
    elif current_page == "Contact Me":
        contact_me()

def display_stars(level):
    star_emoji = "⭐"
    stars = star_emoji * level
    return stars

def about_me():

    st.header("About Me")

    # Alternatively, you can use st.image directly to center
    st.image("tada.jpg", width=150)

    # Personal Introduction
    st.write("Welcome to my portfolio. As a Cultural Broker in the healthcare industry, I am dedicated to delivering culturally responsive services tailored to the unique needs of the Karen community dealing with chemical and mental health issues. Eager to acquire new skills and unlock my full potential through continuous learning and professional development.")
    
    # Skills Section
    st.subheader("Skills")

    # Technology Skills
    with st.expander("Technology Skills"):
        st.info("Microsoft Word")
        st.info("Excel")
        st.info("PowerPoint")
        st.info("Outlook")

    # Language Skills
    with st.expander("Language Skills"):
        st.info("Karen")
        st.info("Burmese")
        st.info("English")
        st.info("Thai")

    # Soft Skills
    with st.expander("Soft Skills"):
        st.info("Dedicated")
        st.info("Team Player")
        st.info("Punctual")
        st.info("Good Organizer")
        st.info("Problem Solver")

    # Additional Information
    st.write("Feel free to reach out for more details or with any inquiries.")

def experience():
    st.header("Work Experience")

    # M Health Fairview - Cultural Broker
    with st.expander("M Health Fairview, St. Paul, MN"):
        st.markdown("<div class='work-exp-title'>Cultural Broker</div>", unsafe_allow_html=True)
        st.markdown("""
            <div class='work-exp-details'>
                <p><strong>Date:</strong> Jan 2021 - Dec 2023</p>
                <p><strong>Organization:</strong> M Health Fairview</p>
                <p>Provided culturally specific co-facilitation of Karen Men’s Recovery Outpatient Treatment Program at St. John’s Hospital</p>
                <p>Provided psychoeducation and case management support services. Coordinated services and collaborated with other providers and agencies.</p>
            </div>
        """, unsafe_allow_html=True)

    # Karen Organization of MN
    with st.expander("Karen Organization of Minnesota, Roseville, MN"):
        st.markdown("<div class='work-exp-title'>Community Health Educator</div>", unsafe_allow_html=True)
        st.markdown("""
            <div class='work-exp-details'>
                <p><strong>Date:</strong> May 2016 - Dec 2020</p>
                <p><strong>Organization:</strong> Karen Organization of MN</p>
                <p>Co-developed the Karen Men’s Recovery Outpatient Treatment Program, co-authored the curriculum, and co-facilitated the program at Roselawn Clinic and St. John's Hospital.</p>
                <p>Completed intake assessments and provided psychoeducation for addiction clients and served walk-in clients at the KOM office. Coordinated services and collaborated with other providers and agencies.</p>
            </div>
        """, unsafe_allow_html=True)

    # Wholesale Produce Supply Co
    with st.expander("Wholesale Produce Supply Co, Minneapolis, MN"):
        st.markdown("<div class='work-exp-title'>Production Line</div>", unsafe_allow_html=True)
        st.markdown("""
            <div class='work-exp-details'>
                <p><strong>Date:</strong> July 2011 - June 2014</p>
                <p><strong>Organization:</strong> Wholesale Produce Supply Co</p>
                <p>Package sorting.</p>
            </div>
        """, unsafe_allow_html=True)

    # DARE Network
    with st.expander("DARE Network (Drug Alcohol Recovery and Education Network), Maesariang, Thailand"):
        st.markdown("<div class='work-exp-title'>Program Supervisor</div>", unsafe_allow_html=True)
        st.markdown("""
            <div class='work-exp-details'>
                <p><strong>Date:</strong> 2007-2011</p>
                <p><strong>Organization:</strong> DARE Network</p>
                <p>Monitored field workers, Budget planning and Reporting, and Monthly reports. Annual report, Transportation arrangement for field workers, training for trainers, publish meetings, Seminars, and Annual conferences.</p>
            </div>
        """, unsafe_allow_html=True)

    # Ma La Oon Refugee Camp Committee
    with st.expander("Ma La Oon Refugee Camp Committee, Maesariang, Thailand"):
        st.markdown("<div class='work-exp-title'>Health Coordinator</div>", unsafe_allow_html=True)
        st.markdown("""
            <div class='work-exp-details'>
                <p><strong>Date:</strong> 2006-2008</p>
                <p><strong>Organization:</strong> Ma La Oon Refugee Camp Committee</p>
                <p>Camp sanitation, water sanitation, networking and cooperation with local NGOs and international NGOs, reporting, taking care of chronic patients in camp, health workers' pronation.</p>
            </div>
        """, unsafe_allow_html=True)

    st.header("Education and Training")
    with st.expander("Education"):
        st.markdown("""
            <div class='education-details'>
                <div class='education-item'>
                    Roseville High School Diploma, Roseville, MN
                </div>
                <div class='education-item'>
                    June 2020
                </div>
            </div>

            <div class='education-details'>
                <div class='education-item'>
                    Mae Khong Kah High School Diploma, Maesariang, Thailand
                </div>
                <div class='education-item'>
                    March 1996
                </div>
            </div>
        """, unsafe_allow_html=True)

    # Expander for Training
    with st.expander("Training"):
        st.markdown("""
            <style>
                .highlight {
                    background-color: rgba(52, 152, 219, 0.3); /* Blue with 30% opacity */
                    padding: 10px;
                    border-radius: 5px;
                    margin-bottom: 10px;
                }

                .training-item {
                    margin-bottom: 5px;
                }

                .date-location {
                    font-style: italic;
                    color: #777;
                }
            </style>

            <div class='education-details'>
                <div class='education-item highlight'>
                    Motivation Interviewing Training
                </div>
                <div class='date-location'>
                    November 2019, Roseville, MN
                </div>
            </div>

            <div class='education-details'>
                <div class='education-item highlight'>
                    Van Driver Coach
                </div>
                <div class='date-location'>
                    August 2018, Minnesota, USA
                </div>
            </div>

            <div class='education-details'>
                <div class='education-item highlight'>
                    Recovery Coach Academy Training
                </div>
                <div class='date-location'>
                    March 2018, Minnesota, USA
                </div>
            </div>

            <div class='education-details'>
                <div class='education-item highlight'>
                    Addiction Worker Training of Trainer Coach
                </div>
                <div class='date-location'>
                    December 2009, Thailand
                </div>
            </div>

            <div class='education-details'>
                <div class='education-item highlight'>
                    Child Protection Training
                </div>
                <div class='date-location'>
                    March 2007, Maesariang, Thailand
                </div>
            </div>

            <div class='education-details'>
                <div class='education-item highlight'>
                    Computer Basic Training
                </div>
                <div class='date-location'>
                    April 2006 - June 2006, Maesariang, Thailand
                </div>
            </div>

            <div class='education-details'>
                <div class='education-item highlight'>
                    Leadership and Management Courses
                </div>
                <div class='date-location'>
                    January 2004 - January 2006, Maesariang, Thailand
                </div>
            </div>

            <div class='education-details'>
                <div class='education-item highlight'>
                    Mobile Computer Training
                </div>
                <div class='date-location'>
                    March 2005, Mae La Oon Refugee Camp, Thailand
                </div>
            </div>

            <div class='education-details'>
                <div class='education-item highlight'>
                    Drug Alcohol Recovery Education Training
                </div>
                <div class='date-location'>
                    May 2002 - June 2002, Maesariang, Thailand
                </div>
            </div>

            <div class='education-details'>
                <div class='education-item highlight'>
                    UDHR (Universal Declaration of Human Rights) Training
                </div>
                <div class='date-location'>
                    March 2002, Maesariang, Thailand
                </div>
            </div>
        """, unsafe_allow_html=True)

# Community Section
def community():
    st.header("Volunteer work & Extracurricular Activities")

    # Define CSS style for community entries
    community_entry_style = """
        background-color: rgba(128, 128, 128, 0.2);
        padding: 10px;
        border-radius: 10px;
    """

    # Mobile responsive style
    mobile_responsive_style = """
        @media only screen and (max-width: 600px) {
            .community-entry {
                flex-direction: column;
                margin-bottom: 15px;  /* Add some spacing between entries */
            }
        }
    """

    st.markdown(
        f"""
        <style>
            .community-entry {{
                {community_entry_style}
            }}

            {mobile_responsive_style}
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Create columns for each entry
    col1, col2, col3 = st.columns(3)

    # Midwest North Region - Karen Baptist Church, USA (KBCUSA)
    with col1:
        st.markdown(
            """
            <div class='community-entry'>
                <p><strong>Organization:</strong> Midwest North Region - Karen Baptist Church, USA (KBCUSA) (national organization)</p>
                <p><strong>Date:</strong> 2021-Present</p>
                <p><strong>Role:</strong> Care and Counseling Department, Secretary</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    # Calvary Karen Baptist Church (Committee)
    with col2:
        st.markdown(
            """
            <div class='community-entry'>
                <p><strong>Organization:</strong> Calvary Karen Baptist Church</p>
                <p><strong>Date:</strong> 2018-Present</p>
                <p><strong>Role:</strong> A Communicator between Community and Church leader or Church members as needed.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    # Karen Community of Minnesota (committee)
    with col3:
        st.markdown(
            """
            <div class='community-entry'>
                <p><strong>Organization:</strong> Karen Community of Minnesota</p>
                <p><strong>Date:</strong> 2017-2023</p>
                <p><strong>Role:</strong> Treasurer: accounting and financial reporting</p>
            </div>
            """,
            unsafe_allow_html=True
        )
# Contact Me Section
def contact_me():
    st.header("Contact Me")

    # Phone Expander
    with st.expander("Phone"):
        st.info("657-202-1532")

    # Email Expander
    with st.expander("Email"):
        st.info("tadahray77@gmail.com")

    # Address Expander
    with st.expander("Address"):
        st.info("2858 Chippewa Ave North St. Paul, MN 55109")

        

if __name__ == "__main__":
    main()