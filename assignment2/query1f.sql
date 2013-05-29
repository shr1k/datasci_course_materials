select count(*) from (
select * from
(select * from frequency where term = 'transactions') as txdocs
inner join
(select * from frequency where term = 'world') as worlddocs
on txdocs.docid = worlddocs.docid
)
;
