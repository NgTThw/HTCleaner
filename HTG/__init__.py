import subprocess
import xml.etree.ElementTree as ET
import os
import gc


class HTParking:
    def __init__(self, postgresql_bin: str = None, host: str = None, port: int = None, database: str = None, username: str = None, password: str = None) -> None:
        self._postgresql_bin = r'C:\Program Files (x86)\PostgreSQL\9.3\bin' if postgresql_bin is None else postgresql_bin
        self.database = 'lparkingdb' if database is None else database
        self.host = 'localhost' if host is None else host
        self._port = 5432 if port is None else port
        self.username = 'lparking' if username is None else username
        self._password = 'Lovad.vn2014' if password is None else password
        self.psql = os.path.normcase(os.path.join(self.postgresql_bin, 'psql.exe'))
        os.environ['PGPASSWORD'] = str(self._password)
        self.error = ''
    
    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self, new: str) -> None:
        self._password = new
        os.environ['PGPASSWORD'] = new
    
    @property
    def port(self):
        return self._port

    @port.getter
    def port(self) -> str:
        return self._port

    @port.setter
    def port(self, new: int) -> None:
        self._port = new
    
    @property
    def postgresql_bin(self):
        return self._postgresql_bin
    
    @postgresql_bin.setter
    def postgresql_bin(self, new: str) -> None:
        self._postgresql_bin = new
        self.psql = os.path.normcase(os.path.join(new, 'psql.exe'))


    def get_vehicle_types(self) -> tuple:
        price = self.__query("select setting_xml from price_setting_v2")
        if not price:
            return tuple()
        root = ET.XML(price)
        list_vehicle = []
        for vehicle in root.findall('VehicleType'):
            vehicle_id = vehicle.get('Id', 'N/A')
            vehicle_name = vehicle.get('Type', 'Unknown')
            list_vehicle.append((vehicle_id, vehicle_name))
        tuple_vehicle = tuple(list_vehicle)
        del list_vehicle
        gc.collect()
        return tuple_vehicle

    def get_id_image_exception(self, end_time: str, start_time: str = '') -> tuple:
        if not start_time:
            query = f"""select id, front_image_path, back_image_path, out_front_image_path, out_back_image_path
from counting_in_out_v2
where at_time < '{end_time}' or out_time < '{end_time}'"""
        else:
            query = f"""select id, front_image_path, back_image_path, out_front_image_path, out_back_image_path
from counting_in_out_v2
where (at_time >= '{start_time}' and at_time < '{end_time}') or (out_time >= '{start_time}' and out_time < '{end_time}')"""
        data = []
        for row in self.__query(query).split('\r\n'):
            data.append(tuple(row.split('|')))
        tuple_data = tuple(data[:-1])
        del data
        gc.collect()
        return tuple_data

    def get_id_image_in_out(self, end_time: str, start_time: str = '', vehicle_type: list|tuple = None) -> tuple:
        if not start_time:
            query = f"""select i.id, o.id, i.front_image_path, i.back_image_path, i.vehicle_image_path, o.front_image_path, o.back_image_path, o.vehicle_image_path
from parking_out2 o
inner join parking_in_history i
on o.parking_in_id = i.id
where o.time_out < '{end_time}'"""
        else:
            query = f"""select i.id, o.id, i.front_image_path, i.back_image_path, i.vehicle_image_path, o.front_image_path, o.back_image_path, o.vehicle_image_path
from parking_out2 o
inner join parking_in_history i
on o.parking_in_id = i.id
where o.time_out >= '{start_time}' and o.time_out < '{end_time}'"""
        if vehicle_type:
            if len(vehicle_type) == 1:
                query += f" and o.vehicle_type = '{vehicle_type[0]}'"
            else:
                query += f" and o.vehicle_type in {tuple(vehicle_type)}"
        data = []
        for row in self.__query(query).split('\r\n'):
            data.append(tuple(row.split('|')))
        tuple_data = tuple(data[:-1])
        del data
        gc.collect()
        return tuple_data

    def delete_exception(self, *ids):
        for id_ in ids:
            self.__query(f"delete from counting_in_out_v2 where id = '{id_}'")

    def delete_parking_out(self, *ids):
        for id_ in ids:
            self.__query(f"delete from parking_out2_today where id ='{id_}'; delete from parking_out2 where id = '{id_}'")

    def delete_parking_in(self, *ids):
        for id_ in ids:
            self.__query(f"delete from parking_in_history_today where id ='{id_}'; delete from parking_in_history where id ='{id_}'")


    def __query(self, query: str) -> str:
        if not os.path.isfile(self.psql):
            raise FileNotFoundError(f'No such file or directory "{self.psql}"')
        self.error = ''
        proc = subprocess.Popen(f'"{self.psql}" -d {self.database} -h {self.host} -p {self._port} -U {self.username} -t -A -c "{query}"',
                            **self.subprocess_args())
        out, err = proc.communicate()
        if err:
            self.error = err.decode('utf-8')
        return out.decode('utf-8')

    @staticmethod
    def subprocess_args(include_stdout=True):
        if hasattr(subprocess, 'STARTUPINFO'):
            si = subprocess.STARTUPINFO()
            si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
            env = os.environ
        else:
            si = None
            env = None
        if include_stdout:
            ret = {'stdout': subprocess.PIPE}
        else:
            ret = {}
        ret.update({'stdin': subprocess.PIPE,
                    'stderr': subprocess.PIPE,
                    'startupinfo': si,
                    'env': env})
        return ret
