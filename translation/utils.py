# -*- coding: utf-8 -*-
"""
functions about database
"""
import os
import pandas as pd


def get_comic_id(con, title):
    """
    get comic id from title
    :param con: connection to database
    :param title: title of comic
    :return: comic id
    """
    sql = "SELECT id FROM comics WHERE title = %s;" % title
    result = pd.read_sql(sql, con)
    if result.shape[0] > 0:
        return result["id"][0]
    else:
        return None


def get_volume_id(con, comic_id, volume):
    """
    get volume id from comic_id & volume
    :param con: connection to database
    :param comic_id: comic_id
    :param volume: volume number of comic
    :return: volume_id
    """
    sql = "SELECT id FROM volumes WHERE comic_id = %s AND volume = %s;" %(str(comic_id), str(volume))
    result = pd.read_sql(sql, con)
    if result.shape[0] > 0:
        return result["id"][0]
    else:
        return None


def insert_dict_into_table(con, table, insert_dict):
    """
    insert dict into table
    :param con: connection to database
    :param table: table name
    :param insert_dict: insert dict (ex:{'lang:'ja', 'name':'ドラえもん', , ,}
    """
    cursor = con.cursor()
    placeholders = ', '.join(['%s'] * len(insert_dict))
    columns = ', '.join(insert_dict.keys())
    params = [x for x in insert_dict.values()]
    sql = "INSERT INTO %s ( %s ) VALUES ( %s );" % (table, columns, placeholders)
    cursor.execute(sql, params)
    con.commit()


def insert_images(con, title, volume, dataset_path):
    """
    insert images info of specific volume into database from title & volume
    :param con: connection to database
    :param title: title of comic
    :param volume: volume number of comic
    :param dataset_path: dataset path # absolute path ex) /home/User/...
    """
    # id
    comic_id = get_comic_id(con, title)
    volume_id = get_volume_id(con, comic_id, volume)

    # every volume
    current_path = dataset_path + "/" + title + "/" + title + "_" + str(volume) + "/"
    os.chdir(current_path)
    file_lists_images = os.listdir('./')
    # delete .DS_Store
    if '.DS_Store' in file_lists_images:
        file_lists_images.remove('.DS_Store')

    for file_image in file_lists_images:
        page = int(file_image.split("_")[-1].split(".")[0])
        path = current_path + file_image
        insert_dict = {'volume_id': volume_id, 'path': path, 'page': page}
        insert_dict_into_table(con, 'images', insert_dict)


def insert_all_images(con, title, dataset_path):
    """
        insert all images info into database from title
        :param con: connection to database
        :param title: title of comic
        :param dataset_path: dataset path # absolute path ex) /home/User/...
        """
    # every volume
    current_path = dataset_path + "/" + title + "/"
    os.chdir(current_path)
    folder_lists_volumes = os.listdir('./')
    # delete .DS_Store
    if '.DS_Store' in folder_lists_volumes:
        folder_lists_volumes.remove('.DS_Store')

    for folder_volume in folder_lists_volumes:
        volume = int(folder_volume.split("_")[-1])
        insert_images(con, title, volume, dataset_path)


def insert_volumes(con, title, dataset_path):
    """
    insert volumes info into database from dataset folder
    **attention: In the future, this method will not be used. Data must be inserted manually
    :param con: connection to database
    :param title: title of comic
    :param dataset_path: dataset path # absolute path ex) /home/User/...
    """
    # comic_id
    comic_id = get_comic_id(con, title)

    # every volume
    current_path = dataset_path + "/" + title + "/"
    os.chdir(current_path)
    folder_lists_volumes = os.listdir('./')
    # delete .DS_Store
    if '.DS_Store' in folder_lists_volumes:
        folder_lists_volumes.remove('.DS_Store')

    for folder_volume in folder_lists_volumes:
        volume = int(folder_volume.split("_")[-1])
        insert_dict = {'comic_id': comic_id, 'volume': volume}
        insert_dict_into_table(con, 'volumes', insert_dict)


