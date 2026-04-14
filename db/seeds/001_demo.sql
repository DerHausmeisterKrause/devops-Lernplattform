INSERT INTO tenants(id,name) VALUES ('00000000-0000-0000-0000-000000000001','default');
INSERT INTO roles(name) VALUES ('learner'),('instructor'),('admin');
INSERT INTO feature_flags(key,enabled) VALUES ('multi_tenant',false),('billing',false),('export_import',true);
