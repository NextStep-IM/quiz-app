import os

import pandas as pd
import streamlit as st

@st.cache_data
def load_dataframe(path):
    return pd.read_csv(path)

CSV_FILE = 'quiz_responses.csv'
df = pd.DataFrame(columns=[
        'age',
        'gender',
        'city',
        'civics', # Studied or not
        'edu_bg', # Education Background
        'answer_1',
        'answer_2',
        'answer_3',
        'answer_4',
        'answer_5'
    ])
if os.path.exists(CSV_FILE):
    df = load_dataframe(CSV_FILE)

st.image('good_luck.png', use_container_width=True)
st.markdown(':material/edit: *Note: The answers need not be completely perfect. This quiz is designed to provoke thought and hopefully make the quiz taker participate in betterment of the country.*')
st.text('\n\n')
st.markdown('- - -')

st.text('* --> Required fields')
age = st.text_input('What is your age? *')
gender = st.selectbox('What is your gender? *', ('Male', 'Female', 'Other'), index=None)
city = st.text_input('In which city do you live? *')
civics = st.selectbox('Have you ever studied civics? *', ('Yes', 'No'), index=None)
edu_bg = st.selectbox('What is your educational background? *', ('School', 'College', 'University'), index=None)


scenarios = [
    {
        "key": "a1",
        "title": "Scenario - 1",
        "icon": ":material/cognition:",
        "description": (
            "You are the head of the HR department in a Pakistani company with a religiously diverse workforce. "
            "While the majority of employees are Muslim, some belong to minority faiths. There is a risk that employees "
            "from different backgrounds may face subtle prejudice or exclusion, which could harm team coordination and workplace harmony."
        ),
        "question": (
            "As an HR leader, how would you ensure a respectful and inclusive environment "
            "where employees of all religions can work together with minimal conflict?"
        )
    },
    {
        "key": "a2",
        "title": "Scenario - 2",
        "icon": ":material/cognition:",
        "description": (
            "You are in charge of a NADRA office in a Pakistani city. You notice that some employees unofficially expect "
            "bribes to “speed up” paperwork, and citizens often feel that paying extra is the only way to get anything done."
        ),
        "question": (
            "You are in a position to change this, what measures would you take to stop this practice "
            "and rebuild public trust in your office?"
        )
    },
    {
        "key": "a3",
        "title": "Scenario - 3",
        "icon": ":material/cognition:",
        "description": (
            "In a rural village in Pakistan, most girls drop out of school after grade 5. Elders in the community believe that "
            "girls should stay at home and prepare for marriage rather than continue their education. You have been invited to speak at a village gathering."
        ),
        "question": (
            "How would you approach changing the elders beliefs about girls education, while respecting their cultural values?"
        )
    },
    {
        "key": "a4",
        "title": "Scenario - 4",
        "icon": ":material/cognition:",
        "description": (
            "You have been put in charge of removing the abundant trash from a city in Pakistan. You need funds and manpower "
            "to accomplish this task. After struggling with getting these resources you decide to get them from the citizens living in the city."
        ),
        "question": (
            "How do you convince the citizens to volunteer and/or donate to the effort?"
        )
    },
    {
        "key": "a5",
        "title": "Scenario - 5",
        "icon": ":material/cognition:",
        "description": (
            "You are a university administrator in Pakistan. A student group wants to hold a peaceful event to discuss controversial "
            "social issues, but some staff and students argue that such topics shouldn't be debated publicly. There is fear that the "
            "event might spark division or unrest on campus."
        ),
        "question": (
            "How would you balance the students’ right to express themselves with the need to maintain campus harmony?"
        )
    }
]

answers = {}

for scenario in scenarios:
    st.markdown(f"### **{scenario['icon']} {scenario['title']}**")
    st.markdown(scenario["description"])
    st.markdown(f"#### **:material/help: Question:**  \n{scenario['question']}")
    answers[scenario["key"]] = st.text_area("**Answer:**", height=136, key=scenario["key"])
    st.text('\n\n\n')
    st.markdown('- - -')

if st.button('Submit'):
    if not (age and gender and city and civics and edu_bg):
        st.warning('Please fill all required fields!')
    new_row = {
        'age': age,
        'gender': gender,
        'city': city,
        'civics': civics,
        'edu_bg': edu_bg,
        'answer_1': answers['a1'],
        'answer_2': answers['a2'],
        'answer_3': answers['a3'],
        'answer_4': answers['a4'],
        'answer_5': answers['a5']
    }
    #df.loc[len(df)] = [age, gender, city, civics, edu_bg, answers['a1'], answers['a2'], answers['a3'], answers['a4'], answers['a5']]
    df.append(new_row, ignore_index=True)
    df.to_csv(CSV_FILE)
    st.success('Saved', icon=':material/done_outline:')