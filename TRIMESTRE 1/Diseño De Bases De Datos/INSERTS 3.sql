USE DatStore

--ESTADO
go
insert into ESTADO values ('Activo')
INSERT INTO ESTADO VALUES ('Inactivo')
INSERT INTO ESTADO VALUES ('Domicilio')
INSERT INTO ESTADO VALUES ('En Tienda')
go
--PROVEEDOR
Go
insert into PROVEEDOR VALUES ('Alqueria',1218587457,'Alqueria@gmail.com','calle 3 A 12',1);
insert into PROVEEDOR VALUES ('Parmalat',1032011245,'Parmalat@gmail.com','calle 4 A 14',1);
insert into PROVEEDOR VALUES ('Colombina',1420112457,'Colombina@gmail.com','calle 1',2);
insert into PROVEEDOR VALUES ('Postob�n',1132011245,'Postob�n@gmail.com','calle 2',2);
insert into PROVEEDOR VALUES ('Coca Cola',1032011246,'Coca_Cola@gmail.com','calle 3',1);
insert into PROVEEDOR VALUES ('Crem Helado',1132011246,'Crem_Helado@gmail.com','calle 4',1);
insert into PROVEEDOR VALUES ('Jet',1132111246,'Jet@gmail.com','calle 5',1);
insert into PROVEEDOR VALUES ('Alpina',0000000000,'Alpina@gmail.com','calle 6',2);
insert into PROVEEDOR VALUES ('Bavaria',7777777777,'Bavaria@gmail.com','calle 0',1);
insert into PROVEEDOR VALUES ('Nescaf�',8888888888,'Nescaf�@gmail.com','calle 7',1);
insert into PROVEEDOR values ('Pepsico',9999999999,'papasfritas@gmail.com','calle 10',1)
Go
--TIPO PRODUCTO
GO
INSERT INTO TIPO_PROD VALUES ('Lacteos',1);
INSERT INTO TIPO_PROD VALUES ('Golosinas',1);
INSERT INTO TIPO_PROD VALUES ('Licores',1);
INSERT INTO TIPO_PROD VALUES ('Bebidas',1);
GO
--ROL
GO
INSERT INTO ROL VALUES ('Admin');
INSERT INTO ROL VALUES ('Empleado');
INSERT INTO ROL VALUES ('Cliente');
GO
--FORMA DE PAGO
GO
INSERT INTO FORMA_PAGO VALUES ('Tarteja Debito',1);
INSERT INTO FORMA_PAGO VALUES ('Tarteja Credito',1);
INSERT INTO FORMA_PAGO VALUES ('Efectivo',1);
INSERT INTO FORMA_PAGO VALUES ('Nequi',1);
INSERT INTO FORMA_PAGO VALUES ('Daviplata',1);
GO 
--USUARIO
GO
INSERT INTO USUARIO VALUES (10051512,'Lionel_ronaldo','l123','CALLE 7','Lionel@gmail.com',7891234567,1,1);
INSERT INTO USUARIO VALUES (9515154,'Pedro_lopez','p123','CALLE 9','Pedro@gmail.com',7823234597,1,3);
INSERT INTO USUARIO VALUES (79964122,'Elonk.musk','e123','CALLE 8','Elonk@tesla.com',7234567,1,2);
INSERT INTO USUARIO VALUES (12254546,'Bill_gates','b123','CALLE 10','bill@gmail.com',7891234587,2,2);
INSERT INTO USUARIO VALUES (49865521,'Jeff_bezos','j123','CALLE 6','jeff@gmail.com',7890234567,2,2);
INSERT INTO USUARIO VALUES (52846103,'Daniel_Rodrigues','d123','CALLE 5','daniel@gmail.com',1891234567,1,3);
INSERT INTO USUARIO VALUES (105164521,'Armando.Paredes','a123','CALLE 4','armando@gmail.com',2891234567,1,3);
INSERT INTO USUARIO VALUES (79512006,'Cristiano.messi','c123','CALLE 1','cris@gmail.com',7891234569,1,1);
INSERT INTO USUARIO VALUES (453151031,'Alam_brito','a123','CALLE 2','Alam@gmail.com',1891234568,2,3);
INSERT INTO USUARIO VALUES (796352035,'Jose.gomez','jo123','CALLE 3','jose@gmail.com',1001010110,1,3);
INSERT INTO USUARIO VALUES (523457869,'Didier_Qui�ones','didisthebest','CALLE 0','didi@gmail.com',1003034712,1,3);
INSERT INTO USUARIO VALUES (212347894,'Omar_Arangure','mainpoppy','CALLE 0.1','despleyxen@gmail.com',1023451245,1,3);
INSERT INTO USUARIO VALUES (758921654,'Daniel_Vergara','crepperowman','CALLE 0.3','danielpug@gmail.com',2301256617,1,3);
INSERT INTO USUARIO VALUES (854968912,'Charles_Miranda','fortinaiti','CALLE 0.3','charlesM@gmail.com',2301256617,1,3);
INSERT INTO USUARIO VALUES (352164321,'Brayan_Mayers','miami12','CALLE 12','brayan@gmail.com',3001063322,1,3);
Go
--PRODUCTO
GO
INSERT INTO PRODUCTO VALUES ('Leche Deslactosada (Alqueria) 500gm',1,1,1);
INSERT INTO PRODUCTO VALUES ('Helado Casero 3 Leches',3,6,1);
INSERT INTO PRODUCTO VALUES ('Cerveza Aguila 250ml',4,4,1);
INSERT INTO PRODUCTO VALUES ('Leche Entera(parmalat)',1,6,1);
INSERT INTO PRODUCTO VALUES ('Aguardiente Antioque�o 1l',4,7,1);
INSERT INTO PRODUCTO VALUES ('Chocolatina Jet 50gr',4,8,1);
INSERT INTO PRODUCTO VALUES ('Manimoto 20gr',2,9,1);
INSERT INTO PRODUCTO VALUES ('Cafe Instantaneo 10mg',1,10,1);
INSERT INTO PRODUCTO VALUES ('Cerveza poker 350ml',4,9,1);
INSERT INTO PRODUCTO VALUES ('Cerveza tecate 350ml',4,9,2);
INSERT INTO PRODUCTO VALUES ('Cerveza Coste�a Bacana',4,9,1);
INSERT INTO PRODUCTO VALUES ('Cerveza Club Colombia',4,9,1);
INSERT INTO PRODUCTO VALUES ('Speedmax',4,4,1);
INSERT INTO PRODUCTO VALUES ('Cerveza Corona 330ml',4,9,2);
INSERT INTO PRODUCTO VALUES ('Chocolotina Jumbo 50gr',3,7,1);
INSERT INTO PRODUCTO VALUES ('Colombiana 350ml',4,4,2);
INSERT INTO PRODUCTO VALUES ('Gaseosa Sabor uva 350ml',4,4,1);
INSERT INTO PRODUCTO VALUES ('Natu malta 350ml',4,4,2);
INSERT INTO PRODUCTO VALUES ('Coca cola 350ml',4,5,1);
INSERT INTO PRODUCTO VALUES ('Fanta 350ml',4,5,1);
INSERT INTO PRODUCTO VALUES ('Cuatro 350ml',4,5,2);
INSERT INTO PRODUCTO VALUES ('Gaseosa Manzana 2L',4,5,2);
INSERT INTO PRODUCTO VALUES ('Pepsi 350ml',4,5,1);
INSERT INTO PRODUCTO VALUES ('Fanta lata 354ml',4,5,2);
INSERT INTO PRODUCTO VALUES ('Natu malta 1L',4,5,1);
INSERT INTO PRODUCTO VALUES ('Coca cola 1.5L',4,5,1);
INSERT INTO PRODUCTO VALUES ('Doritos Flamin Hot 175gr',3,11,2);
INSERT INTO PRODUCTO VALUES ('Doritos 175 gr',3,11,1);
INSERT INTO PRODUCTO VALUES ('Cheetos 44gr',3,11,2);
INSERT INTO PRODUCTO VALUES ('Cheetos Flamin hot',3,11,1);
INSERT INTO PRODUCTO VALUES ('Cheetos boliquesos 160gr',3,11,1);
INSERT INTO PRODUCTO VALUES ('Cheetos trissitos picantes',3,11,1);
GO
--INVENTARIO
GO
INSERT INTO INVENTARIO VALUES (1,500,1);
INSERT INTO INVENTARIO VALUES (2,20,2);
INSERT INTO INVENTARIO VALUES (3,100,3);
INSERT INTO INVENTARIO VALUES (4,10,4);
INSERT INTO INVENTARIO VALUES (5,150,5);
INSERT INTO INVENTARIO VALUES (6,120,6);
INSERT INTO INVENTARIO VALUES (7,10,7);
INSERT INTO INVENTARIO VALUES (8,50,8);
INSERT INTO INVENTARIO VALUES (9,100,9);
INSERT INTO INVENTARIO VALUES (10,70,10);
INSERT INTO INVENTARIO VALUES (12,25,12);
INSERT INTO INVENTARIO VALUES (13,35,13);
INSERT INTO INVENTARIO VALUES (14,45,14);
INSERT INTO INVENTARIO VALUES (15,55,15);
INSERT INTO INVENTARIO VALUES (16,65,16);
INSERT INTO INVENTARIO VALUES (17,10,17);
INSERT INTO INVENTARIO VALUES (18,12,18);
INSERT INTO INVENTARIO VALUES (19,13,19);
INSERT INTO INVENTARIO VALUES (20,4,20);
INSERT INTO INVENTARIO VALUES (21,24,21);
INSERT INTO INVENTARIO VALUES (22,95,22);
INSERT INTO INVENTARIO VALUES (23,85,23);
INSERT INTO INVENTARIO VALUES (24,35,24);
INSERT INTO INVENTARIO VALUES (25,75,25);
INSERT INTO INVENTARIO VALUES (26,45,26);
INSERT INTO INVENTARIO VALUES (27,65,27);
INSERT INTO INVENTARIO VALUES (28,75,28);
INSERT INTO INVENTARIO VALUES (29,85,29);
INSERT INTO INVENTARIO VALUES (30,65,30);
INSERT INTO INVENTARIO VALUES (31,35,31);
INSERT INTO INVENTARIO VALUES (32,25,32);
GO
--ENTRADA INVENTARIO
GO
INSERT INTO ENT_INVENTARIO VALUES (2,'29/03/2022',3,2600,31200,1,10051512);
INSERT INTO ENT_INVENTARIO VALUES (5,'13/10/2020',4,1100,13200,1,79512006);
INSERT INTO ENT_INVENTARIO VALUES (6,'04/01/2022',2,200,1400,2,10051512);
INSERT INTO ENT_INVENTARIO VALUES (3,'05/02/2020',8,100,800,1,79512006);
INSERT INTO ENT_INVENTARIO VALUES (1,'13/10/2020',1,150,3000,1,10051512);
INSERT INTO ENT_INVENTARIO VALUES (7,'10/12/2021',3,600,1200,2,79512006);--
INSERT INTO ENT_INVENTARIO VALUES (10,'29/08/2022',2,500,5000,1,79512006);
INSERT INTO ENT_INVENTARIO VALUES (5,'19/12/2022',7,1500,15000,2,10051512);
INSERT INTO ENT_INVENTARIO VALUES (6,'30/11/2021',2,2000,10000,1,79512006);
INSERT INTO ENT_INVENTARIO VALUES (12,'24/01/2020',8,10000,100000,1,79512006);
INSERT INTO ENT_INVENTARIO VALUES (7,'12/06/2020',10,14000,98000,1,79512006);
INSERT INTO ENT_INVENTARIO VALUES (3,'15/10/2020',1,150,600,1,79512006);
INSERT INTO ENT_INVENTARIO VALUES (7,'26/11/2022',5,100,700,1,10051512);
INSERT INTO ENT_INVENTARIO VALUES (19,'04/04/2022',5,100,1900,2,10051512);
INSERT INTO ENT_INVENTARIO VALUES (26,'16/07/2020',2,1600,41600,1,10051512);
INSERT INTO ENT_INVENTARIO VALUES (5,'10/10/2021',30,5600,28000,1,79512006);
INSERT INTO ENT_INVENTARIO VALUES (7,'16/07/2020',25,1600,11200,1,10051512);
INSERT INTO ENT_INVENTARIO VALUES (1,'05/07/2022',20,1600,1600,2,10051512);
INSERT INTO ENT_INVENTARIO VALUES (15,'10/10/2021',32,2200,33000,1,79512006);
INSERT INTO ENT_INVENTARIO VALUES (10,'16/07/2020',31,1100,11000,1,79512006);
INSERT INTO ENT_INVENTARIO VALUES (16,'26/09/2021',29,5600,89600,2,10051512);
INSERT INTO ENT_INVENTARIO VALUES (5,'26/09/2021',24,4000,20000,1,10051512);
INSERT INTO ENT_INVENTARIO VALUES (20,'12/06/2020',24,4000,8000,1,10051512);
INSERT INTO ENT_INVENTARIO VALUES (12,'24/05/2021',3,3900,46800,1,10051512);
INSERT INTO ENT_INVENTARIO VALUES (17,'18/08/2022',5,500,8500,2,79512006);
INSERT INTO ENT_INVENTARIO VALUES (25,'05/05/2021',2,500,12500,2,79512006);
INSERT INTO ENT_INVENTARIO VALUES (15,'20/03/2021',4,100,1500,2,79512006);
INSERT INTO ENT_INVENTARIO VALUES (10,'28/07/2020',9,1000,10000,2,79512006);
GO
--SALIDA INVENTARIO
GO
INSERT INTO SAL_INVENTARIO VALUES (20,'07/06/2021',3,1000,20000,1,10051512);
INSERT INTO SAL_INVENTARIO VALUES (10,'07/06/2021',4,1100,11000,2,79512006);
INSERT INTO SAL_INVENTARIO VALUES (7,'08/11/2022',2,200,1400,2,79512006);
INSERT INTO SAL_INVENTARIO VALUES (10,'05/06/2021',8,100,1000,1,10051512);
INSERT INTO SAL_INVENTARIO VALUES (5,'08/02/2020',1,150,750,2,79512006);
INSERT INTO SAL_INVENTARIO VALUES (3,'06/06/2020',3,600,1800,2,79512006);
INSERT INTO SAL_INVENTARIO VALUES (10,'02/07/2022',2,500,5000,1,10051512);
INSERT INTO SAL_INVENTARIO VALUES (10,'01/07/2022',7,1500,15000,2,79512006);
INSERT INTO SAL_INVENTARIO VALUES (5,'02/07/2022',2,2000,10000,2,79512006);
INSERT INTO SAL_INVENTARIO VALUES (10,'04/10/2021',8,10000,100000,1,10051512);
INSERT INTO SAL_INVENTARIO VALUES (30,'06/05/2020',30,1000,30000,1,49865521);
INSERT INTO SAL_INVENTARIO VALUES (70,'04/10/2021',15,1000,15000,2,79964122);
INSERT INTO SAL_INVENTARIO VALUES (2,'06/05/2020',5,2500,5000,1,79512006);
INSERT INTO SAL_INVENTARIO VALUES (8,'05/12/2022',5,3000,24000,1,79512006);
INSERT INTO SAL_INVENTARIO VALUES (10,'06/06/2022',5,3500,35000,1,79512006);
INSERT INTO SAL_INVENTARIO VALUES (2,'02/01/2020',30,7000,14000,1,10051512);
INSERT INTO SAL_INVENTARIO VALUES (1,'07/06/2022',25,150,150,3,10051512);
INSERT INTO SAL_INVENTARIO VALUES (6,'01/02/2022',26,200,1200,2,10051512);
INSERT INTO SAL_INVENTARIO VALUES (5,'01/11/2020',20,1400,7000,1,10051512);
INSERT INTO SAL_INVENTARIO VALUES (45,'03/04/2022',20,1400,7000,1,79964122);
INSERT INTO SAL_INVENTARIO VALUES (12,'03/04/2022',12,1000,12000,4,79964122);
INSERT INTO SAL_INVENTARIO VALUES (1,'05/03/2022',5,1500,1500,1,352164321);
INSERT INTO SAL_INVENTARIO VALUES (5,'08/10/2022',5,1500,7500,1,352164321);
INSERT INTO SAL_INVENTARIO VALUES (10,'05/03/2022',7,2000,20000,1,212347894);
INSERT INTO SAL_INVENTARIO VALUES (15,'07/01/2022',10,500,7500,4,854968912);
INSERT INTO SAL_INVENTARIO VALUES (5,'01/03/2022',4,1000,5000,1,758921654);
INSERT INTO SAL_INVENTARIO VALUES (2,'11/03/2022',2,200,400,1,758921654);
INSERT INTO SAL_INVENTARIO VALUES (6,'07/01/2022',16,500,3000,4,854968912);
INSERT INTO SAL_INVENTARIO VALUES (6,'09/04/2021',5,1500,7500,1,523457869);
INSERT INTO SAL_INVENTARIO VALUES (20,'02/02/2022',7,2000,40000,1,523457869);
GO
--PEDIDO
GO
INSERT INTO PEDIDO VALUES ('12/03/2021','En tienda',25000,12254546,4,1);
INSERT INTO PEDIDO VALUES ('03/07/2022','Domicilio',20000,105164521,2,2);
INSERT INTO PEDIDO VALUES ('01/05/2021','En tienda',45000,12254546,3,2);
INSERT INTO PEDIDO VALUES ('07/12/2021','En tienda',25000,105164521,2,1);
INSERT INTO PEDIDO VALUES ('02/11/2020','Domicilio',95000,105164521,1,2);
INSERT INTO PEDIDO VALUES ('07/05/2022','En tienda',55000,52846103,3,1);
INSERT INTO PEDIDO VALUES ('04/07/2022','Domicilio',35000,12254546,4,1);
INSERT INTO PEDIDO VALUES ('05/07/2020','Domicilio',5000,52846103,4,1);
INSERT INTO PEDIDO VALUES ('01/11/2020','En tienda',500,105164521,2,2);
INSERT INTO PEDIDO VALUES ('08/02/2020','Domicilio',200,52846103,4,2);
INSERT INTO PEDIDO VALUES ('08/08/2022','Domicilio',15000,453151031,1,1);
INSERT INTO PEDIDO VALUES ('04/06/2020','En tienda',1000,453151031,1,1);
INSERT INTO PEDIDO VALUES ('07/11/2022','Domicilio',80000,796352035,4,2);
INSERT INTO PEDIDO VALUES ('08/11/2020','En tienda',20000,796352035,3,2);
INSERT INTO PEDIDO VALUES ('03/08/2021','En tienda',700000,105164521,2,3);
INSERT INTO PEDIDO VALUES ('04/02/2020','Domicilio',7000,854968912,4,3);
INSERT INTO PEDIDO VALUES ('05/04/2020','Domicilio',50000,352164321,3,3);
INSERT INTO PEDIDO VALUES ('04/07/2021','En tienda',80000,212347894,2,3);
INSERT INTO PEDIDO VALUES ('04/07/2021','Domicilio',100000,212347894,2,3);
INSERT INTO PEDIDO VALUES ('08/01/2020','En tienda',500000,52846103,2,3);
INSERT INTO PEDIDO VALUES ('08/01/2020','Domicilio',300000,758921654,2,3);
INSERT INTO PEDIDO VALUES ('08/01/2020','En tienda',200000,854968912,2,3);
INSERT INTO PEDIDO VALUES ('08/01/2020','En tienda',700000,9515154,1,3);
INSERT INTO PEDIDO VALUES ('08/01/2020','Domicilio',1000000,212347894,1,3);
INSERT INTO PEDIDO VALUES ('04/02/2021','Domicilio',2000000,796352035,1,3);
INSERT INTO PEDIDO VALUES ('07/03/2022','En tienda',3000000,523457869,1,3);
INSERT INTO PEDIDO VALUES ('09/10/2021','En tienda',10000,212347894,1,3);
GO
--DETALLE PEDIDO Y SALIDA INVENTARIO
GO
INSERT INTO DET_PED_INV VALUES (2,8)
INSERT INTO DET_PED_INV VALUES (2,6)
INSERT INTO DET_PED_INV VALUES (5,7)
INSERT INTO DET_PED_INV VALUES (6,10)
INSERT INTO DET_PED_INV VALUES (5,13)
INSERT INTO DET_PED_INV VALUES (6,15)
INSERT INTO DET_PED_INV VALUES (7,9)
INSERT INTO DET_PED_INV VALUES (8,12)
INSERT INTO DET_PED_INV VALUES (10,8)
INSERT INTO DET_PED_INV VALUES (9,8)
INSERT INTO DET_PED_INV VALUES (3,8)
INSERT INTO DET_PED_INV VALUES (4,8)
INSERT INTO DET_PED_INV VALUES (6,8)
GO
--DOMICILIO
GO
INSERT INTO DOMICILIO VALUES (7,2,'Calle 50a sur #79-03', '02/11/2020'); 
INSERT INTO DOMICILIO VALUES (8,1,'Carrera 90 #2a-27', '28/11/2020');
INSERT INTO DOMICILIO VALUES (9,1,'Transversal 74 #43bis a sur-39', '30/11/2020');
INSERT INTO DOMICILIO VALUES (10,2,'Dig 12 #40-34sur', '12/12/2020');
INSERT INTO DOMICILIO VALUES (12,1,'Carrera 94c #6a-79', '11/11/2020');
INSERT INTO DOMICILIO VALUES (12,1,'Calle 1bis #4-23', '14/11/2020');
INSERT INTO DOMICILIO VALUES (13,2,'Transversal 80 #19-03', '18/12/2020');
INSERT INTO DOMICILIO VALUES (14,2,'Calle 120 sur #10-12', '28/11/2020');
INSERT INTO DOMICILIO VALUES (15,1,'Carrera 200 #20-02', '30/11/2020');
INSERT INTO DOMICILIO VALUES (10,2,'Calle 220 #79-30', '19/11/2020');
INSERT INTO DOMICILIO VALUES (15,2,'Calle 70 A Noroeste', '01/11/2021');
INSERT INTO DOMICILIO VALUES (14,2,'Calle 40 A Suroeste', '12/11/2020');
INSERT INTO DOMICILIO VALUES (12,1,'Calle 80 A sur', '01/09/2021');
INSERT INTO DOMICILIO VALUES (18,2,'Calle 20 A Norte', '05/01/2021');
INSERT INTO DOMICILIO VALUES (20,1,'Calle 10 A occidente', '04/09/2022');
INSERT INTO DOMICILIO VALUES (21,1,'Calle 30 A Norte', '07/04/2020');
INSERT INTO DOMICILIO VALUES (22,2,'Calle 5 A Oeste', '06/05/2021');
INSERT INTO DOMICILIO VALUES (22,2,'Calle 3 A sur', '08/06/2020');
INSERT INTO DOMICILIO VALUES (22,2,'Calle 4 A Norte', '01/05/2020');
INSERT INTO DOMICILIO VALUES (22,2,'Calle 5 A Occidente', '04/04/2022');
INSERT INTO DOMICILIO VALUES (25,2,'Calle 4 A Oeste', '02/01/2022');
INSERT INTO DOMICILIO VALUES (27,2,'Calle 7 A Sur', '07/05/2020');
INSERT INTO DOMICILIO VALUES (24,2,'Calle 5 A Norte', '04/01/2022');
INSERT INTO DOMICILIO VALUES (21,2,'Calle 3 B Oeste', '01/01/2022');
INSERT INTO DOMICILIO VALUES (20,2,'Calle 2 A Sur', '04/04/2020');
INSERT INTO DOMICILIO VALUES (17,2,'Calle 5 C Oeste', '02/02/2021');
INSERT INTO DOMICILIO VALUES (19,2,'Calle 5 F Occidente', '03/03/2020');
INSERT INTO DOMICILIO VALUES (23,2,'Calle 5 D Oeste', '07/07/2020');
INSERT INTO DOMICILIO VALUES (24,2,'Calle 8 A Sur', '06/06/2021');
INSERT INTO DOMICILIO VALUES (25,2,'Calle 5 H Occidente', '06/02/2021');
GO

--Revisar tablas
Select * from PRODUCTO
Select * from USUARIO
Select * from SAL_INVENTARIO
Select * from PEDIDO
Select * from DOMICILIO