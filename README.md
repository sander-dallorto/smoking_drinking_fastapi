# Predição de Riscos de Saúde Usando o Dataset Smoking Drinking

## Descrição do Projeto

Este projeto tem como objetivo prever se um paciente apresenta riscos de saúde com base em diversas informações, como idade, sexo, índice de massa corporal (BMI), entre outros. O modelo foi desenvolvido utilizando o algoritmo de regressão logística, que é adequado para problemas de classificação binária.

## Dataset

O dataset utilizado para este projeto, conhecido como **Smoking Drinking**, contém informações de saúde de pacientes. As principais variáveis (features) consideradas incluem:

- **sex**: Sexo do paciente.
- **age_group**: Faixa etária do paciente.
- **bmi**: Índice de Massa Corporal.
- **waistline**: Medida da cintura.
- **sight_left**: Acuidade visual do olho esquerdo.
- **sight_right**: Acuidade visual do olho direito.
- **hear_left**: Acuidade auditiva do ouvido esquerdo.
- **hear_right**: Acuidade auditiva do ouvido direito.
- **triglyceride**: Nível de triglicerídeos.
- **hemoglobin**: Nível de hemoglobina no sangue.
- **urine_protein**: Presença de proteína na urina.
- **serum_creatinine**: Nível de creatinina sérica.
- **sgot_ast**: Nível de SGOT (AST).
- **sgot_alt**: Nível de SGPT (ALT).
- **gamma_gtp**: Nível de GGT.
- **smk_stat_type_cd**: Código de status de fumo.
- **drk_yn**: Indicador de consumo de álcool (sim/não).
- **bp_ratio**: Proporção da pressão arterial.
- **hdl_ratio**: Proporção de HDL.
- **ldl_ratio**: Proporção de LDL.

## Algoritmo

Para a previsão dos riscos de saúde, foi utilizado o algoritmo de **Regressão Logística**. Esse método é eficaz para classificar dados em duas categorias e é amplamente utilizado em problemas de saúde.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação para desenvolvimento do modelo.
- **Pandas**: Biblioteca para manipulação de dados.
- **Scikit-learn**: Biblioteca para implementação do modelo de regressão logística.
- **FastAPI**: Framework utilizado para criar uma API que realiza a predição.
- **Pickle**: Biblioteca para serialização do modelo treinado.
- **Pydantic**: Biblioteca utilizada para validação de dados de entrada na API.
