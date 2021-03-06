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

    {% if "Y" in  data["NO_PIG"] %}
    document.getElementById("no_pig").checked = true
    {% endif %}
    {% if "Y" in  data["NO_MEAT"] %}
    document.getElementById("no_meat").checked = true
    {% endif %}
    {% if "Y" in  data["NO_CHICKEN"] %}
    document.getElementById("no_chicken").checked = true
    {% endif %}
    {% if "Y" in  data["HALAL"] %}
    document.getElementById("halal").checked = true
    {% endif %}
    {% if "Y" in  data["MANGSA"] %}
    document.getElementById("mangsa").checked = true
    {% endif %}
    {% if "Y" in  data["VEGETARIAN"] %}
    document.getElementById("vegetarian").checked = true
    {% endif %}
    {% if "Y" in  data["ISLAM"] %}
    document.getElementById("islam").checked = true
    {% endif %}
    {% if "Y" in  data["NO_SEAFOOD"] %}
    document.getElementById("no_seafood").checked = true
    {% endif %}
    {% if "Y" in  data["NO_SHRIMP"] %}
    document.getElementById("no_shrimp").checked = true
    {% endif %}
    {% if "Y" in  data["NO_FISH"] %}
    document.getElementById("no_fish").checked = true
    {% endif %}
    
}
