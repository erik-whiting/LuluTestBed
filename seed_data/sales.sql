DO $$
BEGIN
  FOR counter IN 1..100 LOOP
    INSERT INTO Sale (Id, DateOfSale) VALUES (counter, RandomDate());
    INSERT INTO LineItem (SaleId, AlbumId, Price) VALUES 
      (counter, (RANDOM()*(66-2)+2)::INT, 20*random()::decimal(12,2)::MONEY);
    INSERT INTO LineItem (SaleId, AlbumId, Price) VALUES 
      (counter, (RANDOM()*(66-2)+2)::INT, 20*random()::decimal(12,2)::MONEY);
    INSERT INTO LineItem (SaleId, AlbumId, Price) VALUES 
      (counter, (RANDOM()*(66-2)+2)::INT, 20*random()::decimal(12,2)::MONEY);
  END LOOP;
END; $$