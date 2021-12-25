import streamlit as st
import matplotlib.pyplot as plt
import random
import numpy as np
from model import model


# ==============================
# Session init
# ==============================
if 'journal' not in st.session_state:
    st.session_state.journal = {'table': [
                                        ]
                                   }

# ==============================
# Sidebar
# ==============================

st.sidebar.markdown('<p style="text-align: center; padding-right:0%; padding-left:0%"><img src="https://toplogos.ru/images/thumbs/preview-logo-mgu.png", width=50%/></p>', 
            unsafe_allow_html=True)

col1, col2 = st.sidebar.columns([2,1])
col1.markdown(r"<div style='margin-top:55px;text-align:right;'><hr /></div>", unsafe_allow_html=True)
lang = col2.selectbox("", ["RU", "ENG"])

works = {'Работа №1':'Определение ускорения свободного падения с помощью оборотного и математического маятников', 
         'Работа №2':'Какая-то еще работа', 
         'Работа №3':'Какая-то еще работа',
         }
tab_selected = st.sidebar.selectbox('Выберете работу:', works.keys())

# ==============================
# Main page
# ==============================

if tab_selected == list(works.keys())[0]:

    header_container = st.container()
    introduction_container = st.container()
    basics_container = st.container()
    practice_container = st.container()
    results_container = st.container()
    whatnext_container = st.container()

    with header_container:
        st.header(list(works.keys())[0])
        st.subheader(list(works.values())[0])
        '''***'''

    with introduction_container:
        st.subheader('Описание работы')
        col1, col2 = st.columns([1,2])
        col1.image('./Picture_1.png')
        col2.write('Математический маятник - материальная точка, подвешенная на нерастяжимой нити')
        col2.write('Физический маятник - любое тело, имеющее ось вращения ...')
        '''***'''

    with basics_container:
        st.subheader('Цель работы')
        '''
        ознакомиться с закономерностями колебаний математического и физического \
        маятников и с одним из способов определения свободного падения
        '''
        st.subheader('Описание метода измерений')
        '''
        В большинстве методов измерения ускорения свободного падения *g* используется \
        зависимость периода *T* колебаний маятника от величины *g*, так как период колебаний \
        можно измерить с высокой точностью.  
        *Для математического маятника:*  
        $$T=2\pi\sqrt{l/g}$$,  
        где *l* - длина маятника
        '''
        '''
        ...
        '''
        '''
        ...
        '''

    with practice_container:
        st.subheader('Практическая часть')
        '''
        **Задание 1**. Определение ускорения свободного падения с помощью математического маятника
        '''
        '''
        Приведите виртуальный маятник в движение, отклонив его на 5-10° от положения равновесия. 
        Введите заданное число в соответствующее поле. Введите длину матяника.  
        Измерьте время полных пяти колебаний по графику.  
        Запишите результаты измерений и внесите в таблицу.  
        '''
        col1, col2, col3  = st.columns(3)
        angle = col1.number_input('Угол отклонения маятника:', min_value=5.0, max_value=10.0, step=0.1)
        length = col2.number_input('Длина маятника:', min_value=5, max_value=100, step=1)

        if st.button('Calculate'):
            t = np.linspace(0, 20, 1000)
            error = random.random()/100*10 - 0.05
            x = model(t, angle, length, error)
            fig, ax = plt.subplots()
            ax.plot(t,x)
            st.pyplot(fig)
        
        with st.expander('Результаты измерений'):
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                length = st.number_input('l, м', min_value=5, max_value=100, step=1)
            with col2:
                time = st.number_input('t, c', min_value=0,  step=1)
            with col3:
                periods_n = st.number_input('N', min_value=0, step=1)
            with col4:
                period = st.number_input('T, c', min_value=0.0, step=0.1)    
        
            if st.button('Внести результаты'):
                st.session_state.journal['table'].append([length, time, periods_n, period])

        st.table(st.session_state.journal['table'])

        if st.button('Отобразить график'):
            res_T = []
            for row in st.session_state.journal['table']:
                res_T.append(row[-1])

            fig, ax = plt.subplots()
            ax.plot(res_T)
            st.pyplot(fig)

    with results_container:
        st.subheader('Результаты работы')
        answer = st.number_input('Введите ответ:')
        conclusion = st.text_area('Выводы:')

    if st.button('Проверка результатов'):
        if answer != 1:
            st.write('Неверный ответ!')
        else: st.write('Верный ответ!')
        if len(conclusion)<100:
            st.write('Не достаточно развернутые выводы!')

