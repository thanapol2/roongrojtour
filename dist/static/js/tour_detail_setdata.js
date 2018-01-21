function setData() {
    document.getElementById('title_th').value="{{ data["THAI_TITLE"] }}"
    document.getElementById('title_en').value="{{ data["ENG_TITLE"] }}"
    document.getElementById('country').value="{{ data["COUNTRY"] }}"
    document.getElementById('nationality').value="{{ data["NATIONALITY"] }}"
    document.getElementById('province').value="{{ data["PROVINCE"] }}"
    {% if "M" in  data["SEX"] %}
    document.getElementById("male").checked = true
    {% elif "F" in data["SEX"] %}
    document.getElementById("female").checked = true
    {% endif %}
    
}
