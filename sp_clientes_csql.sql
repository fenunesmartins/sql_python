USE [python_sql]
GO
/****** Object:  StoredProcedure [dbo].[CLIENTES_C]    Script Date: 31/08/2021 16:07:33 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
ALTER PROCEDURE [dbo].[CLIENTES_C]
@Id_venda int,
@cliente varchar(50)NULL,
@produto varchar(50) NULL,
@data_venda date NULL,
@preco decimal(6,2) NULL,
@quantidade int NULL
AS
BEGIN
INSERT INTO Vendas (id_venda, cliente, produto, data_venda, preco, quantidade)
VALUES (@Id_venda, @cliente, @produto, @data_venda,@preco,@quantidade)
END

