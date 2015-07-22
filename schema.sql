drop table if exists link;
	create table link (
		id integer primary key autoincrement,
		key text not null,
		url text not null,
		hits integer not null
);