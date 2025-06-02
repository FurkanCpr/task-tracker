import streamlit as st
import requests
import json

# API endpoint'leri
API_URL = "http://127.0.0.1:8000"

st.title("Görev Takip Uygulaması")

# Yeni görev oluşturma formu
st.header("Yeni Görev Ekle")
with st.form("task_form"):
    title = st.text_input("Görev Başlığı")
    description = st.text_area("Görev Açıklaması")
    submit_button = st.form_submit_button("Görev Ekle")

    if submit_button and title and description:
        try:
            response = requests.post(
                f"{API_URL}/tasks/",
                json={"title": title, "description": description}
            )
            if response.status_code == 200:
                st.success("Görev başarıyla eklendi!")
            else:
                st.error("Görev eklenirken bir hata oluştu.")
        except Exception as e:
            st.error(f"Bağlantı hatası: {str(e)}")

# Mevcut görevleri listeleme
st.header("Mevcut Görevler")
try:
    response = requests.get(f"{API_URL}/tasks/")
    if response.status_code == 200:
        tasks = response.json()
        if tasks:
            for task in tasks:
                with st.expander(f"{task['title']}"):
                    st.write(f"Açıklama: {task['description']}")
                    if st.button(f"Sil", key=f"delete_{task['id']}"):
                        delete_response = requests.delete(f"{API_URL}/tasks/{task['id']}")
                        if delete_response.status_code == 200:
                            st.success("Görev silindi!")
                            st.rerun()
                        else:
                            st.error("Görev silinirken bir hata oluştu.")
        else:
            st.info("Henüz görev bulunmuyor.")
    else:
        st.error("Görevler alınırken bir hata oluştu.")
except Exception as e:
    st.error(f"Bağlantı hatası: {str(e)}") 