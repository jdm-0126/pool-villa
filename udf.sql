-- udf_booking_get_all
CREATE OR REPLACE FUNCTION public.udf_booking_get_all(
      p_param VARCHAR(10) default ''
) RETURNS TABLE (
  id INT,
  name VARCHAR(255),
  address VARCHAR(255),
  description TEXT,
  imagePath VARCHAR(255) ,
  price VARCHAR(255) ,
  isAvailable INT
) AS $func$
BEGIN
  RETURN QUERY
  SELECT
    b.id AS id,
    b."name" AS name,
    b."address" AS address,
    b."description" AS description,
    b."imagePath" AS imagePath,
    b."price" AS price,
    b."isAvailable" AS isAvailable
      FROM pv_info AS b where CAST("isAvailable" AS TEXT) LIKE '%' || p_param || '%';
END;
$func$ LANGUAGE plpgsql;

-- udf_booking_save
CREATE OR REPLACE FUNCTION public.udf_booking_save(
  p_name VARCHAR,
  p_address VARCHAR,
  p_description TEXT,
  p_imagePath VARCHAR,
  p_price VARCHAR
	) RETURNS INTEGER AS $func$
BEGIN
  
  INSERT INTO "pv_info"("name","address","description","imagePath","price","isAvailable") VALUES(p_name,p_address,p_description,p_imagePath,p_price,1);
  
   RETURN NULL;
END;
$func$ LANGUAGE plpgsql;

-- udf_booking_update

CREATE OR REPLACE FUNCTION public.udf_booking_update(
  p_id INT,
  p_name VARCHAR(255),
  p_address VARCHAR(255),
  p_description VARCHAR(255) ,
  p_imagePath VARCHAR(255) ,
  p_price VARCHAR(255) 
) RETURNS INTEGER AS $func$
BEGIN
  
  UPDATE pv_info SET "name" =p_name,"address"=p_address,"description" =p_description,"imagePath" =p_imagePath,"price" =p_price WHERE id = p_id;
  
  RETURN NULL;
END;
$func$ LANGUAGE plpgsql;

--udf_booking_info

CREATE OR REPLACE FUNCTION public.udf_booking_info(
      p_param VARCHAR(255) default ''
) RETURNS TABLE (
  id INT,
  firstName VARCHAR(255),
  lastName VARCHAR(255),
  email VARCHAR(255),
  mobileNo VARCHAR(255) ,
  poolVillaId INT,
  checkIn DATE,
  checkOut DATE,
  isPaid INT
) AS $func$
BEGIN
  RETURN QUERY
  SELECT
    b.id AS id,
    b."firstName" AS firstName,
    b."lastName" AS lastName,
    b."email" AS email,
    b."mobileNo" AS mobileNo,
    b."poolVillaId" AS poolVillaId,
    b."checkIn" AS checkIn,
    b."checkOut" AS checkOut,
    b."isPaid" AS isPaid
      FROM pv_booking_info AS b where CAST(b."email" AS TEXT) LIKE '%' || p_param || '%';
END;
$func$ LANGUAGE plpgsql;