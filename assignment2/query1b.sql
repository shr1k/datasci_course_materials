select count(*) from (
select distinct term from frequency where docid = '10398_txt_earn' and count=1
);
