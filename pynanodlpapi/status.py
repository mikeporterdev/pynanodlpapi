class NanoDlpPrinterStatus:
    def __init__(self, raw: dict):
        self._raw = raw

    @property
    def auto_shutdown(self) -> bool:
        return self._raw.get("AutoShutdown")
    
    @property
    def build(self) -> str:
        return self._raw.get("Build")
    
    @property
    def camera(self) -> int:
        return self._raw.get("Camera")
    
    @property
    def cast(self) -> bool:
        return self._raw.get("Cast")

    @property
    def covered(self) -> bool:
        return self._raw.get("Covered")
    
    @property
    def current_height(self) -> int:
        return self._raw.get("CurrentHeight")
    
    @property
    def force_stop(self) -> bool:
        return self._raw.get("ForceStop")

    @property
    def halted(self) -> bool:
        return self._raw.get("Halted")

    @property
    def hostname(self) -> str:
        return self._raw.get("Hostname")

    @property
    def ip(self) -> str:
        return self._raw.get("IP")
    
    @property
    def lamp_hours(self) -> int:
        return self._raw.get("LampHours")
    
    @property
    def layer_id(self) -> int:
        return self._raw.get("LayerID")

    @property
    def layer_since_start(self) -> int:
        return self._raw.get("LayerSinceStart")
    
    @property
    def layer_since_time(self) -> int:
        return self._raw.get("LayerSinceTIme")

    @property
    def layer_time(self) -> int:
        return self._raw.get("LayerTime")
    
    @property
    def layers_count(self) -> int:
        return self._raw.get("LayersCount")
    
    @property
    def panic_row(self) -> int:
        return self._raw.get("PanicRow")

    @property
    def panicked(self) -> bool:
        return self._raw.get("Panicked")
    
    @property
    def path(self) -> str:
        return self._raw.get("Path")

    @property
    def paused(self) -> bool:
        return self._raw.get("Paused")

    @property
    def plate_height(self) -> float:
        return self._raw.get("PlateHeight")
    
    @property
    def plate_id(self) -> int:
        return self._raw.get("PlateID")

    @property
    def prev_layer_time(self) -> int:
        return self._raw.get("PrevLayerTime")

    @property
    def printing(self) -> bool:
        return self._raw.get("Printing")

    @property
    def real_time_est(self) -> bool:
        return self._raw.get("RealTimeEst")
    
    @property
    def resin_level_mm(self) -> bool:
        return self._raw.get("ResinLevelMm")

    @property
    def resume_id(self) -> int:
        return self._raw.get("ResumeID")

    @property
    def slicing_plate_id(self) -> int:
        return self._raw.get("SlicingPlateID")
    
    @property
    def start_after_slice(self) -> int:
        return self._raw.get("StartAfterSlice")

    @property
    def state(self) -> int:
        return self._raw.get("State")

    @property
    def version(self) -> int:
        return self._raw.get("Version")

    @property
    def Wifi(self) -> str:
        return self._raw.get("Wifi")

    @property
    def disk(self) -> str:
        return self._raw.get("disk")
    
    @property
    def mcu(self) -> int:
        return self._raw.get("mcu")

    @property
    def mem(self) -> str:
        return self._raw.get("mem")

    @property
    def proc(self) -> str:
        return self._raw.get("proc")

    @property
    def proc_numb(self) -> str:
        return self._raw.get("proc_numb")

    @property
    def resin(self) -> int:
        return self._raw.get("resin")

    @property
    def started(self) -> int:
        return self._raw.get("started")

    @property
    def temp(self) -> str:
        return self._raw.get("temp")
    
    @property
    def uptime(self) -> str:
        return self._raw.get("uptime")