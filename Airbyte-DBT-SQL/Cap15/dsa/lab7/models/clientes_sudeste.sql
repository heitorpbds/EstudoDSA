{{ config(materialized='view') }}  -- Configura o modelo para ser materializado como uma "view" no banco de dados

WITH clientes_sudeste AS (  
    SELECT *
    FROM {{ref('clientes')}}  -- Referencia o modelo "clientes" para obter os dados base
    WHERE estado IN ('SP', 'RJ', 'MG', 'ES')  -- Filtra apenas os clientes dos estados do Sudeste
)

SELECT * FROM clientes_sudeste