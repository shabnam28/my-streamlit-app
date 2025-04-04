import streamlit as st


#Set app to wide mode
st.set_page_config(layout="wide")
#title of our app
st.title("Questionnaire de Maturité RSE")
# Info Société
st.header("Info Société")
raison_sociale = st.selectbox("1. Raison Sociale", ["Asso", "Entreprise", "Collectivité territoriale"])
nb_collaborateurs = st.number_input("2. Nb Collaborateurs/habitants ?", min_value=0,max_value=50000000,value=18)
st.write(f"Nombre de collaborateurs : {nb_collaborateurs}")
ca = st.number_input("3. CA (in k€) ?", min_value=0,max_value=100000000,value=50)
bilan = st.number_input("4. Bilan (in k€) ?", min_value=0,max_value=100000000, value=500)
secteur = st.selectbox("5. Secteur?", ["Oil&Gaz", "Finance", "BTP", "AgroAlimentaire", "Transport/Mobilité", "Textile", "Autre-Industrie", "Autre-Service"])

# Maturité : Sensibilisation
st.header("Maturité : Sensibilisation")
comite_sensibilise = st.radio("6. Votre comité de direction est-il déjà sensibilisé aux enjeux énergie/climat et sociaux ?", options=["Oui", "Non"],horizontal=True)
organisation_sensibilise_management = st.radio("7. Votre organisation souhaite-t-elle sensibiliser aux enjeux énergie/climat et sociaux - Votre Management ?", options=["Oui", "Non"],horizontal=True)
organisation_sensibilise_collaborateurs = st.radio("8. Votre organisation souhaite-t-elle sensibiliser aux enjeux énergie/climat et sociaux - L’ensemble de vos collaborateurs ?", options=["Oui", "Non"],horizontal=True)
formation_experts = st.radio("9. Votre organisation souhaite-t-elle former des experts de la transition pour internaliser les études RSE ? (Finance durable, comptabilité carbone, ...)", options=["Oui", "Non"],horizontal=True)

# Maturité : Identification Enjeux RSE
#st.header("Maturité : Identification Enjeux RSE")
enjeux_rse_identifies = st.radio("10. Votre organisation a-t-elle déjà identifié ses enjeux RSE prioritaires ? (A travers un Diag ISO26000, une cartographie des parties prenantes, une analyse de contexte sectoriel et concurrentiel, une analyse des risques intangiles,...)", options=["Oui", "Non"],horizontal=True)
feuille_de_route = st.radio("11. Votre organisation a-t-elle déjà défini une feuille de route ? (Engagements et Actions prioritaires)", options=["Oui", "Non"],horizontal=True)

# Maturité : Bilan Carbone
#st.header("Maturité : Bilan Carbone")
estimation_ges = st.radio("12. Votre organisation a-t-elle déjà réalisé une première estimation d'emissions GES ?", options=["Oui", "Non"],horizontal=True)
bilan_ges_complet = st.radio("13. Votre organisation a-t-elle déjà réalisé un Bilan GES complet (Scopes 123) sur l’ensemble de votre structure (toutes filiales comprises) de moins de 3ans ?", options=["Oui", "Non"],horizontal=True)
plan_reduction_carbone = st.radio("14. L'entreprise a-t-elle défini un plan de réduction des émissions carbone à horizon 2030?", options=["Oui", "Non"],horizontal=True)
saas_kpi_environnementaux = st.radio("15. L'entreprise a-t-elle mis en place un Saas pour collecter et suivre ses KPI environnementaux ?", options=["Oui", "Non"],horizontal=True)
engagement_sbti = st.radio("16. L'entreprise a-t-elle pris un engagement SBTi vers la neutralité carbone ?", options=["Oui", "Non"],horizontal=True)

# Maturité : Rapport RSE
#st.header("Maturité : Rapport RSE")
rapport_rse = st.radio("17. Votre organisation a-t-elle déjà rédigé un rapport RSE de moins de 5ans ?", options=["Oui", "Non"],horizontal=True)
analyse_materialite_simple = st.radio("18. Votre organisation a-t-elle déjà réalisé une analyse de Simple Matérialité ?", options=["Oui", "Non"],horizontal=True)
analyse_materialite_double = st.radio("19. Votre organisation a-t-elle déjà réalisé une analyse de Double Matérialité ?", options=["Oui", "Non"],horizontal=True)
analyse_iro = st.radio("20. Votre organisation a-t-elle déjà réalisé une analyse IRO de vos Enjeux RSE ?", options=["Oui", "Non"],horizontal=True)
risques_climatiques_physiques = st.radio("21. Votre organisation a-t-elle déjà réalisé une analyse de risques climatiques physiques ?", options=["Oui", "Non"],horizontal=True)
conformite_csrd = st.radio("22. Etes-vous déjà en conformité avec la CSRD ?", options=["Oui", "Non"],horizontal=True)

# Maturité : Labels & EcoVadis
#st.header("Maturité : Labels & EcoVadis")
notation_ecovadis = st.radio("23. Votre organisation a-t-elle déjà une notation Ecovadis ?", options=["Oui", "Non"],horizontal=True)
label_rse = st.radio("24. Votre organisation a-t-elle déjà un label RSE ?", options=["Oui", "Non"],horizontal=True)

# Ressources
st.header("Ressources")
temps_plein_rse = st.selectbox("25. De combien d’'Equivalent Temps Plein' disposez-vous pour travailler vos sujets RSE ? (Chiffre)", ["Référent temps partiel", "Chef de projet", "Equipe de 2", "Equipe de 3 ou plus"])
dispo_etudes = st.selectbox("26. Quelles sont leur dispo pour participer aux études ?", ["Transmettre les données RSE ?", "Centraliser les infos et coordonner le projet ?", "Produire des parties d’études ?", "Pleine implication pour se former pour internaliser les choses dans le futur)"])
ambition_demarche = st.selectbox("27.Quelle est l'ambition de votre démarche RSE ?", ["Premiers études pour ESTIMATION des ordres de grandeur et comformité réglementaire ?", "Etude complète pour communication et image ?", "Etude précises pour planifier votre transition 2030 ?", "Être précurseur et planifier sa transition NetZero 2050 ?"])
raison_demarche = st.selectbox("28. La raison principale de votre démarche RSE ?", ["Règlementation ?", "Demandes Clients (AO)/ partenaires / invest? ", "Conviction Environnementale et Sociale ?"])
budget_rse = st.number_input("29. Quel est votre budget pour une démarche RSE en k€?", min_value=0,max_value=100000000,value=50)

# Calcul des scores (à compléter)
if st.button("Calculer la Maturité"):
    # Logique de scoring basée sur les réponses (à implémenter)
    st.write("Résultats du calcul de la maturité (à implémenter)")
