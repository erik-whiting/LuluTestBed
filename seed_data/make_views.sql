CREATE VIEW TrackList AS
  SELECT
    b.BandName AS "Band",
    b.id AS BandId,
    al.AlbumName AS "Album",
    al.releasedate AS "ReleaseDate",
    al.id AS AlbumId,
    s.SongName AS "Track"
  FROM Song s
    INNER JOIN Album al
    ON s.albumid = al.id
    INNER JOIN Band b
    ON al.bandid = b.id
  ORDER BY "ReleaseDate";


  CREATE VIEW SaleTotals AS
    SELECT s.DateOfSale, SUM(li.Price)
    FROM Sale s
    JOIN LineItem li ON li.SaleId = s.Id
    GROUP BY s.Id
    ORDER BY s.DateOfSale DESC;
