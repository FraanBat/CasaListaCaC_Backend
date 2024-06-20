DROP DATABASE casalista;
CREATE DATABASE casalista;

INSERT INTO usuarios(nombre, apellido, mail, contrasena, zona, telefono, genero, imagen, profesion_id, descripcion_profesional) VALUES ("Jorge", "Perez", "jorge@codoacodo.com.ar", "12345678", "Boedo", 1553319259,"M", "https://previews.dropbox.com/p/thumb/ACRv-U9jsFqaAqPn2ytGOPu_DD0o27c3s3oL78EswZvz6L_rXWdOr8VRbzdGpBgoGyiRb0CrM-x8D7QKu9_nffBCpQOWRJW9BCAZnmhyG_o1w4SDYTudwe7AJoFag3AwZ9gJXYNTT4_FsS6XDMyRhJbAFXeWysfi2ku9W52_1uTYmyhTC37ZIk0YhY_orKWbCPhnBGp4QQlm-GvfZaPnjt6GmMvxeXkeC73XwhW_2vfBCGzhgUvru5BKEtngtKWlMbO5k3KPEwC2EbmufID6Bq9M2B04-l86gdr3GtLqxXntCmO3YQoBYtBROcle5Muh5vimow2nXqg-Q2MkDfiUwTr6/p.jpeg", 2, "Más de 5 años de experiencia")

INSERT INTO usuarios(nombre, apellido, mail, contrasena, zona, telefono, genero, imagen, profesion_id, descripcion_profesional) VALUES ("Juan", "Alvarez", "juan@codoacodo.com.ar", "12345678", "Boedo", 1553319259,"M", "https://previews.dropbox.com/p/thumb/ACRv-U9jsFqaAqPn2ytGOPu_DD0o27c3s3oL78EswZvz6L_rXWdOr8VRbzdGpBgoGyiRb0CrM-x8D7QKu9_nffBCpQOWRJW9BCAZnmhyG_o1w4SDYTudwe7AJoFag3AwZ9gJXYNTT4_FsS6XDMyRhJbAFXeWysfi2ku9W52_1uTYmyhTC37ZIk0YhY_orKWbCPhnBGp4QQlm-GvfZaPnjt6GmMvxeXkeC73XwhW_2vfBCGzhgUvru5BKEtngtKWlMbO5k3KPEwC2EbmufID6Bq9M2B04-l86gdr3GtLqxXntCmO3YQoBYtBROcle5Muh5vimow2nXqg-Q2MkDfiUwTr6/p.jpeg", 2, "Renombre en la zona")

INSERT INTO usuarios(nombre, apellido, mail, contrasena, zona, telefono, genero, imagen) VALUES ("Luis", "Suarez", "luis@gmail.com", "12345678", "Boedo", 1553319259, "M", "https://previews.dropbox.com/p/thumb/ACRvi2SeT3fl2PuAUPr17jIal3UkVeFcJI-ZKjm2acjnJgktnHd-IBDZwVIjva98c5er4oO2C6-uymzFtpfgGu9hYcFW-tGwIdUiJhbpa4P0Xa35EHTNo2Yu2x0c3H76farQjFsExtao_aXRNgiZqwnOX9VRYgYAdubNIi4yxM6wybhb64TeaxEgS0mGC7IE3f8V3bonqPQgVtyuKMSiItlHLqqmkNIzaW8YUu5n4O7tW9PrE-FWSKQsFEN8wlmBqrMWy9rl5T_DCEw_rynuB9-I7aClqiIwgO4Y5iIGFSDHVZasZ2EeoYm7bE4ITKi8sbVvagSokvT132vJEOcRMR9x/p.jpeg")

INSERT INTO usuarios(nombre, apellido, mail, contrasena, zona, telefono, genero, imagen, profesion_id, descripcion_profesional) VALUES ("Micaela", "Gutierrez", "micaela@codoacodo.com.ar", "12345678", "Chacarita", 1553319259,"M", "https://previews.dropbox.com/p/thumb/ACRv-U9jsFqaAqPn2ytGOPu_DD0o27c3s3oL78EswZvz6L_rXWdOr8VRbzdGpBgoGyiRb0CrM-x8D7QKu9_nffBCpQOWRJW9BCAZnmhyG_o1w4SDYTudwe7AJoFag3AwZ9gJXYNTT4_FsS6XDMyRhJbAFXeWysfi2ku9W52_1uTYmyhTC37ZIk0YhY_orKWbCPhnBGp4QQlm-GvfZaPnjt6GmMvxeXkeC73XwhW_2vfBCGzhgUvru5BKEtngtKWlMbO5k3KPEwC2EbmufID6Bq9M2B04-l86gdr3GtLqxXntCmO3YQoBYtBROcle5Muh5vimow2nXqg-Q2MkDfiUwTr6/p.jpeg", 6, "Trabajo a bajo costo")

USE casalista;
SELECT * FROM usuarios;
SELECT * FROM profesion;
SELECT * FROM pedidos;

INSERT INTO profesion(profesion) VALUES ("Electicista");
INSERT INTO profesion(profesion) VALUES ("Gasista");
INSERT INTO profesion(profesion) VALUES ("Plomero");
INSERT INTO profesion(profesion) VALUES ("Carpintero");
INSERT INTO profesion(profesion) VALUES ("Jardinero");
INSERT INTO profesion(profesion) VALUES ("Cerrajero");
INSERT INTO profesion(profesion) VALUES ("Aire acondicionado");
INSERT INTO profesion(profesion) VALUES ("Pintor");
INSERT INTO profesion(profesion) VALUES ("Albañil");
INSERT INTO profesion(profesion) VALUES ("Fletero");