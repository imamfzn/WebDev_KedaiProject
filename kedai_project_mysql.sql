/*==============================================================*/
/* DBMS name:      MySQL 5.0                                    */
/* Created on:     28/12/2016 13:53:07                          */
/*==============================================================*/


drop table if exists customer_service;

drop table if exists gedung;

drop table if exists kurir;

drop table if exists menu;

drop table if exists menu_harian;

drop table if exists pelanggan;

drop table if exists pesanan;

drop table if exists suplier;

/*==============================================================*/
/* Table: customer_service                                      */
/*==============================================================*/
create table customer_service
(
   id_cs                int not null auto_increment,
   nama_cs              varchar(50) not null,
   primary key (id_cs)
);

/*==============================================================*/
/* Table: gedung                                                */
/*==============================================================*/
create table gedung
(
   nama_gedung          varchar(50) not null,
   id_gedung            int not null auto_increment,
   primary key (id_gedung)
);

/*==============================================================*/
/* Table: kurir                                                 */
/*==============================================================*/
create table kurir
(
   id_kurir             int not null auto_increment,
   nama_kurir           varchar(50) not null,
   primary key (id_kurir)
);

/*==============================================================*/
/* Table: menu                                                  */
/*==============================================================*/
create table menu
(
   nama_menu            varchar(50) not null,
   harga_menu           int not null,
   id_menu              int not null auto_increment,
   id_suplier           smallint not null,
   deskripsi_menu       text,
   foto_menu            varchar(100),
   primary key (id_menu)
);

/*==============================================================*/
/* Table: menu_harian                                           */
/*==============================================================*/
create table menu_harian
(
   tanggal              date not null,
   id_menu_harian       int not null auto_increment,
   id_menu              int not null,
   primary key (id_menu_harian)
);

/*==============================================================*/
/* Table: pelanggan                                             */
/*==============================================================*/
create table pelanggan
(
   nama_pelanggan       varchar(50) not null,
   id_pelanggan         int not null auto_increment,
   id_gedung            int not null,
   no_hp_pelanggan      char(15) not null,
   keterangan_lokasi    varchar(50) not null,
   primary key (id_pelanggan)
);

/*==============================================================*/
/* Table: pesanan                                               */
/*==============================================================*/
create table pesanan
(
   id_pelanggan         int not null,
   id_menu_harian       int not null,
   id_pesanan           int not null auto_increment,
   waktu_pemesanan      time not null,
   jumlah_pesanan       int not null,
   status_pesanan       char(16) not null,
   id_cs                int,
   id_kurir             int,
   primary key (id_pesanan)
);

/*==============================================================*/
/* Table: suplier                                               */
/*==============================================================*/
create table suplier
(
   nama_suplier         varchar(50) not null,
   alamat_suplier       varchar(100) not null,
   id_suplier           smallint not null auto_increment,
   primary key (id_suplier)
);

alter table menu add constraint fk_memiliki foreign key (id_suplier)
      references suplier (id_suplier) on delete restrict on update restrict;

alter table menu_harian add constraint fk_tersedia foreign key (id_menu)
      references menu (id_menu) on delete restrict on update restrict;

alter table pelanggan add constraint fk_berada_di foreign key (id_gedung)
      references gedung (id_gedung) on delete restrict on update restrict;

alter table pesanan add constraint fk_dipesan foreign key (id_menu_harian)
      references menu_harian (id_menu_harian) on delete restrict on update restrict;

alter table pesanan add constraint fk_memesan foreign key (id_pelanggan)
      references pelanggan (id_pelanggan) on delete restrict on update restrict;

alter table pesanan add constraint fk_mengantar foreign key (id_kurir)
      references kurir (id_kurir) on delete restrict on update restrict;

alter table pesanan add constraint fk_mengelola foreign key (id_cs)
      references customer_service (id_cs) on delete restrict on update restrict;

