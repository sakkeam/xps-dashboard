import subprocess

import streamlit as st


def main():
    st.title("XPS dashboard")

    st.header("ThermalManagement")

    quiet_clicked = st.button("Quiet")
    ultra_performance_clicked = st.button("UltraPerformance")

    st.header("PrimaryBattChargeCfg")

    adaptive_clicked = st.button("Adaptive")
    prim_ac_use_clicked = st.button("PrimAcUse")

    cctk = "C:\\Program Files (x86)\\Dell\\Command Configure\\X86_64\\cctk.exe"

    if quiet_clicked:
        sudo([cctk, "--ThermalManagement=Quiet"])

    if ultra_performance_clicked:
        sudo([cctk, "--ThermalManagement=UltraPerformance"])

    if adaptive_clicked:
        sudo([cctk, "--PrimaryBattChargeCfg=Adaptive"])

    if prim_ac_use_clicked:
        sudo([cctk, "--PrimaryBattChargeCfg=PrimAcUse"])


def sudo(args: list[str]) -> None:
    subprocess.run(["sudo.exe", *args])


if __name__ == "__main__":
    main()
