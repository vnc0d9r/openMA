import os
import sys
import ConfigParser

from core.color import *

CONFIG_FILE = "openma.conf"

class OpenMAConfig:
    def __init__(self):
        self.config=None

        if os.path.exists(CONFIG_FILE):
            try:
                self.config=ConfigParser.ConfigParser()
                self.config.read(CONFIG_FILE)
            except Exception, why:
                print(red("[Config] [ERROR] Cannot read config file \"%s\": %s."
                    % (CONFIG_FILE,why)))
        else:
            print(red("[Config] [ERROR] Cannot find config file \"%s\"."
                % CONFIG_FILE))          
    
    def write_default_config(self):
        print(green("[Config] [INFO] Write default config \"%s\"." % CONFIG_FILE))
       
        if not self.config:
            self.config=ConfigParser.ConfigParser()

        self.config.add_section("Logging")
        self.config.set('Logging', 'utc', "False")
        self.config.set('Logging', 'path', "log/openma.log")
        self.config.set('Logging', 'debug', "True")

        self.config.add_section("openma1")
        self.config.set('openma1', 'name', "openma1")
        self.config.set('openma1', 'username', "openma")
        self.config.set('openma1', 'password', "openma")   
        self.config.set('openma1', 'share', "shares/openma1")         

        self.config.add_section("VirtualMachines")
        self.config.set('VirtualMachines', 'engine', "VirtualBox")
        self.config.set('VirtualMachines', 'mode', "gui")
        self.config.set('VirtualMachines', 'python', "/usr/bin/python")
        self.config.set('VirtualMachines', 'enabled', "openma1")

        self.config.add_section("Analysis")
        self.config.set('Analysis', 'watchdog_timeout', "600")
        self.config.set('Analysis', 'analysis_timeout', "120")
        self.config.set('Analysis', 'results_path', "analysis/")
        self.config.set('Analysis', 'postprocessing', "processor.py")

        self.config.add_section("LocalDatabase")
        self.config.set('LocalDatabase', 'file', "db/cuckoo.db")

        with open(CONFIG_FILE, 'wb') as configfile:
            self.config.write(configfile)
    
    def _error_parse(self, why):
        print(red("[Config] [ERROR] Error parsing config file: \"%s\": %s."
                    % (CONFIG_FILE, why)))

    def _error_config(self):
        print(red("[Config] [ERROR] ConfigParser not properly initialized."))

    def get_logging_utc(self):
        if self.config:
            try:
                return self.config.get("Logging", "utc")
            except Exception, why:
                self._error_parse(why)
                return None
        else:
            self._error_config()
            return None

    def get_logging_path(self):
        if self.config:
            try:
                return self.config.get("Logging", "path")
            except Exception, why:
                self._error_parse(why)
                return None
        else:
            self._error_config()
            return None

    def get_logging_debug(self):
        if self.config:
            try:
                return self.config.get("Logging", "debug")
            except Exception, why:
                self._error_parse(why)
                return None
        else:
            self._error_config()
            return None

    def get_vm_name(self, vm_id):
        if self.config:
            try:
                return self.config.get(vm_id, "name")
            except Exception, why:
                self._error_parse(why)
                return None
        else:
            self._error_config()
            return None

    def get_vm_username(self, vm_id):
        if self.config:
            try:
                return self.config.get(vm_id, "username")
            except Exception, why:
                self._error_parse(why)
                return None
        else:
            self._error_config()
            return None

    def get_vm_password(self, vm_id):
        if self.config:
            try:
                return self.config.get(vm_id, "password")
            except Exception, why:
                self._error_parse(why)
                return None
        else:
            self._error_config()
            return None

    def get_vm_engine(self):
        if self.config:
            try:
                return self.config.get("VirtualMachines", "engine")
            except Exception, why:
                self._error_parse(why)
                return None
        else:
            self._error_config()
            return None
        
    def get_vm_mode(self):
        if self.config:
            try:
                return self.config.get("VirtualMachines", "mode")
            except Exception, why:
                self._error_parse(why)
                return None
        else:
            self._error_config()
            return None

    def get_vm_python(self):
        if self.config:
            try:
                return self.config.get("VirtualMachines", "python")
            except Exception, why:
                self._error_parse(why)
                return None
        else:
            self._error_config()
            return None

    def get_vm_share(self, vm_id):
        if self.config:
            try:
                return self.config.get(vm_id, "share")
            except Exception, why:
                self._error_parse(why)
                return None
        else:
            self._error_config()
            return None

    def get_vms(self):
        if self.config:
            try:
                return self.config.get("VirtualMachines", "enabled").split(",")
            except Exception, why:
                self._error_parse(why)
                return None
        else:
            self._error_config()
            return None

    def get_analysis_watchdog_timeout(self):
        if self.config:
            try:
                return self.config.get("Analysis", "watchdog_timeout")
            except Exception, why:
                self._error_parse(why)
                return None
        else:
            return None

    def get_analysis_analysis_timeout(self):
        if self.config:
            try:
                return self.config.get("Analysis", "analysis_timeout")
            except Exception, why:
                self._error_parse(why)
                return None
        else:
            return None

    def get_analysis_results_path(self):
        if self.config:
            try:
                return self.config.get("Analysis", "results_path")
            except Exception, why:
                self._error_parse(why)
                return None
        else:
            return None

    def get_analysis_processor(self):
        if self.config:
            try:
                return self.config.get("Analysis", "postprocessing")
            except Exception, why:
                self._error_parse(why)
                return None
        else:
            return None

    def get_localdb(self):
        if self.config:
            try:
                return self.config.get("LocalDatabase", "file")
            except Exception, why:
                self._error_parse(why)
                return None
        else:
            self._error_config()
            return None