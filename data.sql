CREATE TABLE data (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(250) NOT NULL,
    distance_x_cm VARCHAR(60) NOT NULL,
    distance_y_cm VARCHAR(250) NOT NULL,
    goods_received_kg VARCHAR(250) NOT NULL,
    estimated_time VARCHAR(250) NOT NULL,
    lead_time VARCHAR(250) NOT NULL
);


INSERT INTO User (name, distance_x_cm, distance_y_cm, goods_received_kg, estimated_time, lead_time) VALUES
('Logistics distribution center', '9.2', '2.8', '300', '9:00', '19:00'),
('Huangjia Garden', '10', '3', '240', '12:00', '15:00'),
('Taoyuan New Village', '10', '3.6', '145', '13:00', '16:00'),
('Zhong Lanli', '10.8', '3.2', '380', '15:00', '18:00'),
('Zhong Shan Yi Fu', '10.2', '4.6', '150', '13:00', '17:00'),
('Huangpu Garden', '10.4', '5.4', '80', '12:00', '15:00'),
('Huangpu Road No.4 Community', '10', '5.2', '120', '13:00', '16:00'),
('Dongda Yingbi Community', '9.2', '3.6', '360', '14:00', '17:00'),
('Sha Tong Garden', '8.6', '2', '175', '13:00', '16:00'),
('Heung Ju Mei Yuan', '8.2', '1.2', '420', '13:00', '15:00'),
('Kairun Jincheng', '9.4', '0.2', '230', '12:00', '15:00'),
('Yangtze River Garden', '9.4', '0.6', '500', '14:00', '17:00'),
('Beimenqiao Road High-rise', '9', '0.8', '90', '14:00', '18:00'),
('Bluestone Garden', '10.4', '0.6', '140', '15:00', '18:00'),
('Weixiang community', '8.4', '1', '40', '13:00', '16:00'),
('Yi Xiang Community', '8.4', '1.6', '160', '15:00', '18:00'),
('Orchid Garden', '7.8', '3.2', '40', '13:00', '16:00'),
('Yanwu New Village', '8', '3.4', '220', '15:00', '18:00'),
('Taiping Garden', '7.2', '5.2', '300', '13:00', '17:00'),
('Yuexin Garden', '7.6', '5.4', '430', '13:00', '16:00'),
('Qingxi Garden', '10.6', '7', '400', '14:00', '17:00'),
('Jinling Imperial Garden', '6.6', '5', '300', '12:00', '15:00');
