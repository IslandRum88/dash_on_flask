from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

db_host = 'localhost'
db_name = 'cc_db'
db_user = 'dba'
db_password = 'sql'

engine = create_engine(f'mssql+pyodbc://{db_user}:{db_password}@{db_host}/{db_name}?driver=ODBC+Driver+11+for+SQL+Server')
# engine = create_engine(f'mssql+pyodbc://{db_host}/{db_name}?driver=ODBC+Driver+17+for+SQL+Server&Trusted_Connection=yes')

"""
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

SET ANSI_PADDING ON
GO

CREATE TABLE [dbo].[Plotters](
	[Id] [int] NOT NULL,
	[Title] [varchar](100) NOT NULL,
	[CreatedAt] [datetime] NOT NULL,
	[Body] [varchar](100) NULL,
PRIMARY KEY CLUSTERED 
(
	[Id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]

GO

SET ANSI_PADDING OFF
GO

INSERT [dbo].[Plotters] ([Id], [Title], [CreatedAt], [Body]) VALUES (1, N'foo', CAST(N'2021-02-02 18:45:32.053' AS DateTime), N'blahadhasflasdfljk')
GO
INSERT [dbo].[Plotters] ([Id], [Title], [CreatedAt], [Body]) VALUES (2, N'bar', CAST(N'2021-02-02 18:45:32.053' AS DateTime), N'redfoxblaha')
GO
INSERT [dbo].[Plotters] ([Id], [Title], [CreatedAt], [Body]) VALUES (3, N'drew', CAST(N'2021-02-02 18:45:32.053' AS DateTime), N'doctor drew')


"""

Session = sessionmaker(bind=engine)

Base = declarative_base()
