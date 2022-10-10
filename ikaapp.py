import streamlit as st
import random
from random import randint

st.title("イカルーレット")
st.caption('今日の立ち回り決めようや')

h = 'hyousho.txt'
b = 'buki.txt'

with open(h, encoding="utf-8") as f:
    hy = f.readlines()

with open(b, encoding="utf-8") as f:
    bu = f.readlines()

buki_btn = st.button('今日の立ち回りはこれだ！')


if buki_btn:
    buki = random.choice(bu).strip()
    hyosho = random.choice(hy).strip()
    st.text(f'{buki}を使って{hyosho}をとれ！')
    print(bu)
