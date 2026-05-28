create table plantas(
    planta_id serial primary key,
    planta_nome varchar(255) not null,
    planta_nome_cientifico varchar(255) not null,
    planta_descricao text,
    planta_tipo varchar(50) not null,
    planta_nota_verao float,
    planta_nota_outono float,
    planta_nota_inverno float,
    planta_nota_primavera float
)

create table culturas(
    cultura_id serial primary key,
    planta_id int not null,
    cultura_status varchar(50) not null,
    cultura_data_plantio date,
    cultura_data_colheita date,
    foreign key (planta_id) references plantas(planta_id)
)