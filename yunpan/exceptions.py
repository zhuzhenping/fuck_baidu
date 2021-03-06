class LoginError(Exception):
    def __str__(self):
        return "还未登陆或者登陆已经失效"


class LoginFail(Exception):
    def __str__(self):
        return "登录失败，建议官网手动登陆一次"


class UnExceptedException(Exception):
    def __str__(self):
        return "我也不知道是什么引起了这个错误"


class RecodeNotExists(Exception):
    def __init__(self, recode_path: str):
        self.recode_path = recode_path

    def __str__(self):
        return "记录文件不存在，其路径应为{recode_path}".format(
            recode_path=self.recode_path)


class CanNotDownload(Exception):
    def __str__(self):
        return "本方法不支持下载文件夹"


class RemoteFileNotExist(Exception):
    def __init__(self, remote_path: str):
        self.remote_path = remote_path

    def __str__(self):
        return "网盘上没有该文件:{remote_path}".format(remote_path=self.remote_path)


class UnExceptedRemoteReturnErrorMessage(Exception):
    def __init__(self, error_message: str):
        self.error_message = error_message

    def __str__(self):
        return "暂时还没有处理的百度网盘API错误提示，其内容为:{error_message}".format(error_message=self.error_message)


class RemoteFileHasBeenModified(Exception):
    def __str__(self):
        return "远程文件已被修改，请重新下载"


class DownloadFail(Exception):
    def __str__(self):
        return "下载未完成，请重试"


class LocalFileExists(Exception):
    def __init__(self, target_path):
        self.target_path = target_path

    def __str__(self):
        return "所有数据已经下载至临时文件，但目标文件已经存在，请自行确认是否需要替换:{target_path}".format(target_path=self.target_path)


class DownloadInfoUnMatched(Exception):
    def __init__(self, info_path):
        self.info_path = info_path

    def __str__(self):
        return "远程文件已被修改或数据块大小被修改"


class LocalDirPathCanNotSameAsFile(Exception):
    def __init__(self, local_path: str):
        self.local_path = local_path

    def __str__(self):
        return "目标文件夹路径与现存文件相同:{local_path}".format(local_path=self.local_path)


class RemotePathIsFile(Exception):
    def __init__(self, remote_path):
        self.remote_path = remote_path

    def __str__(self):
        return "远程路径对应的是一个文件，无法获取其子目录文件，该路径为{remote_path}".format(remote_path=self.remote_path)
