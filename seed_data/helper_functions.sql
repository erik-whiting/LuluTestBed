CREATE FUNCTION RandomDate() RETURNS DATE AS $$
	BEGIN
		RETURN (timestamp '2020-01-10 20:00:00' + random() * (timestamp '2000-01-20 20:00:00' - timestamp '2020-01-10 10:00:00'))::date;
	END
$$ LANGUAGE plpgsql;

CREATE FUNCTION RandomId() RETURNS INTEGER AS $$
  BEGIN
    RETURN (RANDOM()*(31-1)+1)::INT;
  END
$$ LANGUAGE plpgsql;

CREATE FUNCTION RandomBandId() RETURNS INTEGER AS $$
  BEGIN
    RETURN (RANDOM()*(66-2)+2)::INT;
  END
$$ LANGUAGE plpgsql

