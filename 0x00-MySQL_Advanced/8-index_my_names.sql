-- creates an index on the names table and the first letter names.name

CREATE INDEX idx_name_first ON names (name(1));
