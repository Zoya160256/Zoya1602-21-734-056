import streamlit as st

def main():
    st.title("My Portfolio")

    # Profile Picture
    profile_image = st.file_uploader("Upload Profile Picture", type=["jpg", "png"])
    if profile_image is not None:
        st.image(profile_image, width=150)

    # Header
    name = st.text_input("Enter Your Name:")
    title = st.text_input("Enter Your Professional Title:")

    if name and title:
        st.write(f"""
        # {name}
        {title}
        """)

    # About Me
    st.subheader("About Me")
    about_me = st.text_area("Write About Yourself:")

    # Skills
    st.subheader("Skills")
    skills = st.text_area("Enter Your Skills (One per line):")

    # Projects
    st.subheader("Projects")
    project_name = st.text_input("Enter Project Name:")
    project_description = st.text_area("Describe Your Project:")
    project_image = st.file_uploader("Upload Project Image", type=["jpg", "png"])

    if project_name and project_description and project_image:
        st.subheader(project_name)
        st.write(project_description)
        st.image(project_image, width=300)

    # Achievements
    st.subheader("Achievements")
    achievement_name = st.text_input("Enter Achievement Name:")
    achievement_description = st.text_area("Describe Your Achievement:")
    achievement_image = st.file_uploader("Upload Achievement Image", type=["jpg", "png"])

    if achievement_name and achievement_description and achievement_image:
        st.subheader(achievement_name)
        st.write(achievement_description)
        st.image(achievement_image, width=300)

    # Contact Information
    st.subheader("Contact Information")
    email = st.text_input("Enter Your Email Address:")
    linkedin = st.text_input("Enter Your LinkedIn Profile URL:")

    if email and linkedin:
        st.write(f"Email: {email}")
        st.write(f"LinkedIn: {linkedin}")

if __name__ == "__main__":
    main()
