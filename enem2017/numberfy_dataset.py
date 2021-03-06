import pandas as pd

dataset_path = './microdados_enem2017/DADOS/MICRODADOS_ENEM_2017.csv'
chunksize = 100000

good_columns = [
 'NU_INSCRICAO',
 'NU_ANO',
 'CO_MUNICIPIO_RESIDENCIA',
 'CO_UF_RESIDENCIA',
 'SG_UF_RESIDENCIA',
 'NU_IDADE',
 'TP_SEXO',
 'TP_ESTADO_CIVIL',
 'TP_COR_RACA',
 'TP_NACIONALIDADE',
 'CO_MUNICIPIO_NASCIMENTO',
 'CO_UF_NASCIMENTO',
 'SG_UF_NASCIMENTO',
 'TP_ST_CONCLUSAO',
 'TP_ANO_CONCLUIU',
 'TP_ESCOLA',
 'TP_ENSINO',
 'IN_TREINEIRO',
 'CO_ESCOLA',
 'CO_MUNICIPIO_ESC',
 'CO_UF_ESC',
 'SG_UF_ESC',
 'TP_DEPENDENCIA_ADM_ESC',
 'TP_LOCALIZACAO_ESC',
 'TP_SIT_FUNC_ESC',
 'IN_BAIXA_VISAO',
 'IN_CEGUEIRA',
 'IN_SURDEZ',
 'IN_DEFICIENCIA_AUDITIVA',
 'IN_SURDO_CEGUEIRA',
 'IN_DEFICIENCIA_FISICA',
 'IN_DEFICIENCIA_MENTAL',
 'IN_DEFICIT_ATENCAO',
 'IN_DISLEXIA',
 'IN_DISCALCULIA',
 'IN_AUTISMO',
 'IN_VISAO_MONOCULAR',
 'IN_OUTRA_DEF',
 'IN_GESTANTE',
 'IN_LACTANTE',
 'IN_IDOSO',
 'IN_ESTUDA_CLASSE_HOSPITALAR',
 'IN_SEM_RECURSO',
 'IN_BRAILLE',
 'IN_AMPLIADA_24',
 'IN_AMPLIADA_18',
 'IN_LEDOR',
 'IN_ACESSO',
 'IN_TRANSCRICAO',
 'IN_LIBRAS',
 'IN_LEITURA_LABIAL',
 'IN_MESA_CADEIRA_RODAS',
 'IN_MESA_CADEIRA_SEPARADA',
 'IN_APOIO_PERNA',
 'IN_GUIA_INTERPRETE',
 'IN_COMPUTADOR',
 'IN_CADEIRA_ESPECIAL',
 'IN_CADEIRA_CANHOTO',
 'IN_CADEIRA_ACOLCHOADA',
 'IN_PROVA_DEITADO',
 'IN_MOBILIARIO_OBESO',
 'IN_LAMINA_OVERLAY',
 'IN_PROTETOR_AURICULAR',
 'IN_MEDIDOR_GLICOSE',
 'IN_MAQUINA_BRAILE',
 'IN_SOROBAN',
 'IN_MARCA_PASSO',
 'IN_SONDA',
 'IN_MEDICAMENTOS',
 'IN_SALA_INDIVIDUAL',
 'IN_SALA_ESPECIAL',
 'IN_SALA_ACOMPANHANTE',
 'IN_MOBILIARIO_ESPECIFICO',
 'IN_MATERIAL_ESPECIFICO',
 'IN_NOME_SOCIAL',
 'CO_MUNICIPIO_PROVA',
 'CO_UF_PROVA',
 'SG_UF_PROVA',
 'TP_PRESENCA_CN',
 'TP_PRESENCA_CH',
 'TP_PRESENCA_LC',
 'TP_PRESENCA_MT',
 'NU_NOTA_CN',
 'NU_NOTA_CH',
 'NU_NOTA_LC',
 'NU_NOTA_MT',
 'TP_LINGUA',
 'TP_STATUS_REDACAO',
 'NU_NOTA_COMP1',
 'NU_NOTA_COMP2',
 'NU_NOTA_COMP3',
 'NU_NOTA_COMP4',
 'NU_NOTA_COMP5',
 'NU_NOTA_REDACAO',
 'Q001',
 'Q002',
 'Q003',
 'Q004',
 'Q005',
 'Q006',
 'Q007',
 'Q008',
 'Q009',
 'Q010',
 'Q011',
 'Q012',
 'Q013',
 'Q014',
 'Q015',
 'Q016',
 'Q017',
 'Q018',
 'Q019',
 'Q020',
 'Q021',
 'Q022',
 'Q023',
 'Q024',
 'Q025',
 'Q026',
 'Q027'
]

letter_columns = [
 'Q001',
 'Q002',
 'Q003',
 'Q004',
 'Q006',
 'Q007',
 'Q008',
 'Q009',
 'Q010',
 'Q011',
 'Q012',
 'Q013',
 'Q014',
 'Q015',
 'Q016',
 'Q017',
 'Q018',
 'Q019',
 'Q020',
 'Q021',
 'Q022',
 'Q023',
 'Q024',
 'Q025',
 'Q026',
 'Q027'
]

ufs = [
'AC',
'AL',
'AP',
'AM',
'BA',
'CE',
'ES',
'GO',
'MA',
'MT',
'MS',
'MG',
'PA',
'PB',
'PR',
'PE',
'PI',
'RJ',
'RN',
'RS',
'RO',
'RR',
'SC',
'SP',
'SE',
'TO',
'DF'
]

letter_columns = [
 'Q001',
 'Q002',
 'Q003',
 'Q004',
 'Q006',
 'Q007',
 'Q008',
 'Q009',
 'Q010',
 'Q011',
 'Q012',
 'Q013',
 'Q014',
 'Q015',
 'Q016',
 'Q017',
 'Q018',
 'Q019',
 'Q020',
 'Q021',
 'Q022',
 'Q023',
 'Q024',
 'Q025',
 'Q026',
 'Q027'
]

ufs = [
'AC',
'AL',
'AP',
'AM',
'BA',
'CE',
'ES',
'GO',
'MA',
'MT',
'MS',
'MG',
'PA',
'PB',
'PR',
'PE',
'PI',
'RJ',
'RN',
'RS',
'RO',
'RR',
'SC',
'SP',
'SE',
'TO',
'DF'
]

int_columns = [
 'NU_INSCRICAO',
 'NU_ANO',
 'CO_MUNICIPIO_RESIDENCIA',
 'CO_UF_RESIDENCIA',
 'SG_UF_RESIDENCIA',
 'NU_IDADE',
 'TP_SEXO',
 'TP_ESTADO_CIVIL',
 'TP_COR_RACA',
 'TP_NACIONALIDADE',
 'CO_MUNICIPIO_NASCIMENTO',
 'CO_UF_NASCIMENTO',
 'SG_UF_NASCIMENTO',
 'TP_ST_CONCLUSAO',
 'TP_ANO_CONCLUIU',
 'TP_ESCOLA',
 'TP_ENSINO',
 'IN_TREINEIRO',
 'CO_ESCOLA',
 'CO_MUNICIPIO_ESC',
 'CO_UF_ESC',
 'SG_UF_ESC',
 'TP_DEPENDENCIA_ADM_ESC',
 'TP_LOCALIZACAO_ESC',
 'TP_SIT_FUNC_ESC',
 'IN_BAIXA_VISAO',
 'IN_CEGUEIRA',
 'IN_SURDEZ',
 'IN_DEFICIENCIA_AUDITIVA',
 'IN_SURDO_CEGUEIRA',
 'IN_DEFICIENCIA_FISICA',
 'IN_DEFICIENCIA_MENTAL',
 'IN_DEFICIT_ATENCAO',
 'IN_DISLEXIA',
 'IN_DISCALCULIA',
 'IN_AUTISMO',
 'IN_VISAO_MONOCULAR',
 'IN_OUTRA_DEF',
 'IN_GESTANTE',
 'IN_LACTANTE',
 'IN_IDOSO',
 'IN_ESTUDA_CLASSE_HOSPITALAR',
 'IN_SEM_RECURSO',
 'IN_BRAILLE',
 'IN_AMPLIADA_24',
 'IN_AMPLIADA_18',
 'IN_LEDOR',
 'IN_ACESSO',
 'IN_TRANSCRICAO',
 'IN_LIBRAS',
 'IN_LEITURA_LABIAL',
 'IN_MESA_CADEIRA_RODAS',
 'IN_MESA_CADEIRA_SEPARADA',
 'IN_APOIO_PERNA',
 'IN_GUIA_INTERPRETE',
 'IN_COMPUTADOR',
 'IN_CADEIRA_ESPECIAL',
 'IN_CADEIRA_CANHOTO',
 'IN_CADEIRA_ACOLCHOADA',
 'IN_PROVA_DEITADO',
 'IN_MOBILIARIO_OBESO',
 'IN_LAMINA_OVERLAY',
 'IN_PROTETOR_AURICULAR',
 'IN_MEDIDOR_GLICOSE',
 'IN_MAQUINA_BRAILE',
 'IN_SOROBAN',
 'IN_MARCA_PASSO',
 'IN_SONDA',
 'IN_MEDICAMENTOS',
 'IN_SALA_INDIVIDUAL',
 'IN_SALA_ESPECIAL',
 'IN_SALA_ACOMPANHANTE',
 'IN_MOBILIARIO_ESPECIFICO',
 'IN_MATERIAL_ESPECIFICO',
 'IN_NOME_SOCIAL',
 'CO_MUNICIPIO_PROVA',
 'CO_UF_PROVA',
 'SG_UF_PROVA',
 'TP_PRESENCA_CN',
 'TP_PRESENCA_CH',
 'TP_PRESENCA_LC',
 'TP_PRESENCA_MT',
 'TP_LINGUA',
 'TP_STATUS_REDACAO',
 'Q001',
 'Q002',
 'Q003',
 'Q004',
 'Q005',
 'Q006',
 'Q007',
 'Q008',
 'Q009',
 'Q010',
 'Q011',
 'Q012',
 'Q013',
 'Q014',
 'Q015',
 'Q016',
 'Q017',
 'Q018',
 'Q019',
 'Q020',
 'Q021',
 'Q022',
 'Q023',
 'Q024',
 'Q025',
 'Q026',
 'Q027'
]

int_map = {x : int for x in int_columns}

def drop_rows(df):
    return df.dropna(subset=['NU_NOTA_CN', 'NU_NOTA_CH', 'NU_NOTA_LC', 'NU_NOTA_MT'])

def select_good_columns(df):
    return df.loc[0:,good_columns]

def char_to_code(c):
    if not isinstance(c, str):
        return -1
    return ord(c) - ord('A')

def uffy(s):
    try:
        return ufs.index(s)
    except:
        return -1

def unletterfy(df):
    for cs in letter_columns:
        df[cs] = df[cs].apply(char_to_code)
    df['TP_SEXO'] = df['TP_SEXO'].apply(lambda c: 1 if c == 'M' else 0)
    df['SG_UF_PROVA'] = df['SG_UF_PROVA'].apply(lambda s: ufs.index(s))
    df['SG_UF_NASCIMENTO'] = df['SG_UF_NASCIMENTO'].apply(uffy)
    df['SG_UF_RESIDENCIA'] = df['SG_UF_RESIDENCIA'].apply(uffy)
    df['SG_UF_ESC'] = df['SG_UF_ESC'].apply(uffy)
    return df

def beautify_chunk(df):
    return unletterfy(drop_rows(select_good_columns(df))).fillna(-1).astype(int_map)

with open('./microdados_enem2017/ENEM_2017_INTEGERS.csv', 'a') as f:
    f.write(str.join(',', good_columns) + '\n')
    for df in pd.read_csv(dataset_path, chunksize=chunksize, delimiter=';', encoding='ISO-8859-1'):
        beautify_chunk(df).to_csv(f, header=False, index=False)
        print(len(df), "rows written")
