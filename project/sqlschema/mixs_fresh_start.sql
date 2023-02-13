

CREATE TABLE "Checklists" (
	depth TEXT, 
	PRIMARY KEY (depth)
);

CREATE TABLE "Extension" (
	depth TEXT, 
	PRIMARY KEY (depth)
);

CREATE TABLE "Package" (
	depth TEXT, 
	PRIMARY KEY (depth)
);

CREATE TABLE "QuantityValue" (
	depth TEXT, 
	has_raw_value TEXT, 
	PRIMARY KEY (depth, has_raw_value)
);
