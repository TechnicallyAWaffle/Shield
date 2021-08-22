SYLAS = 370  # Moonstone Renewer + Mejais Soulstealer + Rabadons + Mikael's Blessing + Redemption + Seraph’s Embrace
# SYLAS = 255  # Starcaster + Ardent Censer + Rabadons + Vigilant Wardstone + Redemption + Seraph's Embrace
# SYLAS =  # Starcaster + Meiai's Soulstealer  + Rabadons + Vigilant Wardstone + Redemption + Seraph's Embrace
# SYLAS = # Starcaster + Mejais' Soulstealer + Rabadons + Mikael's Blessing + Redemption + Vigilant Wardstone
SHEN = 365  # Moonstone Renewer + Staff of Flowing Water + Rabadons + Ardent Censer + Redemption + Mikaels Blessing
# SHEN =  # Starcaster + Vigilant Wardstone + Rabadons + Ardent Censer + Redemption + Mikaels Blessing
VIEGO = 1  # Uses possessed champions' items
LULU = 660  # Everfrost + Mejais + Rabadons + Horizon Focus + Nashors Tooth + Seraph's Embrace
# LULU = 620 # Eternal Winter + Mejais + Rabadons + Horizon Focus + Vigilant Wardstone + Seraph's Embrace
# LULU = 460 Starcaster + Mejais Soulstealer + Rabadons + Ardent Censer + Mikaels + Seraph’s Embrace
# LULU = 615  Eternal Winter + Mejais + Rabadons + Seraphs + Ardent Censer + Staff of Flowing Water
LUX = 475  # Everfrost, Mejais, Rabadons, Seraphs, Redemption, Mikaels
# LUX = 505  # Eternal Winter, Vigilant Wardstone, Rabadons, Seraphs, Redemption, Mikaels
IVERN = 475  # Everfrost, Mejais, Rabadons, Seraphs, Redemption, Mikaels
LEE_SIN = 405  # Everfrost, Mejais, Rabadons, Ardent Censer, Mikaels, Redemption
RAKAN = 475  # Everfrost, Mejais, Rabadons, Seraphs, Mikaels, Redemption
TAHM_HEALTH = 2050  # Moonstone Renewer, Redemption, Spirit Visage, Warmogs, Gargoyle Stoneplate
# TAHM_HEALTH = 1500  # Starcaster , Redemption, Spirit Visage, Vigilant Wardstone, Gargoyle Stoneplate
TAHM = 40  # Moonstone Renewer
AP_RUNES = 78  # Double Adaptive + Absolute Focus + Waterwalking
AP_BUFFS = 175  # Baron + Elixir + Staff of Flowing Water
HP_RUNES = 90  # Health Shard
HP_BUFFS = 300  # Elixir of Iron
AP_MULTIPLIER = 0.35  # Rabadons
SHIELD_MULTIPLIER = 0.5  # Revitalize outgoing + Revitalize incoming + Tahm's Revitalize + Spirit Visage
SELF_SHIELD_MULTIPLIER = 0.4  # Revitalize incoming + Revitalize + Spirit Visage


def empyrean(champion):
    global BASE_MANA, MYTHIC, AP, MANAFLOW
    if champion == "sylas":
        BASE_MANA = 1470
        MYTHIC = 0
        AP = SYLAS
        MANAFLOW = 250
    if champion == "lulu":
        BASE_MANA = 1285
        MYTHIC = 600
        AP = LULU
        MANAFLOW = 250
    if champion == "lux":
        BASE_MANA = 879.5
        MYTHIC = 600
        AP = LUX
        MANAFLOW = 0
    if champion == "ivern":
        BASE_MANA = 1470
        MYTHIC = 600
        AP = IVERN
        MANAFLOW = 0
    if champion == "rakan":
        BASE_MANA = 1165
        MYTHIC = 600
        AP = RAKAN
        MANAFLOW = 0
    MANA_PERCENT = (5 + (0.025 * AP)) / 100  # Percent
    return MANA_PERCENT * (
            BASE_MANA + 860 + MANAFLOW + MYTHIC)  # Base Mana + Seraph's Bonus Mana + Manaflow + Mythic(Passives)


def awe(champion):
    global MYTHIC
    if champion == "sylas":
        MYTHIC = 0
    if champion == "lulu":
        MYTHIC = 600
    if champion == "lux":
        MYTHIC = 600
    if champion == "ivern":
        MYTHIC = 600
    if champion == "rakan":
        MYTHIC = 600
    return (empyrean(champion) + 860 + 250 + MYTHIC) * 0.05


def sylas_ap():
    return (SYLAS + awe("sylas") + AP_RUNES + AP_BUFFS) * (1 + AP_MULTIPLIER)


def shen_ap():
    return (SHEN + AP_RUNES + AP_BUFFS) * (1 + AP_MULTIPLIER)


def lulu_ap():
    return (LULU + awe("lulu") + AP_RUNES + AP_BUFFS + 30) * (1 + AP_MULTIPLIER)


def lux_ap():
    return (LUX + awe("lux") + AP_RUNES + AP_BUFFS) * (1 + AP_MULTIPLIER)


def ivern_ap():
    return (IVERN + awe("ivern") + AP_RUNES + AP_BUFFS) * (1 + AP_MULTIPLIER)


def lee_sin_ap():
    return (LEE_SIN + AP_RUNES + AP_BUFFS) * (1 + AP_MULTIPLIER)


def rakan_ap():
    return(RAKAN + awe("rakan") + AP_RUNES + AP_BUFFS) * (1 + AP_MULTIPLIER)


def tahm_kench_health():
    return (2185 + TAHM_HEALTH + HP_RUNES + HP_BUFFS + (600 + (0.5 * lulu_ap()))) * 1.12


def tahm_kench_ap():
    return (TAHM + AP_RUNES + (AP_BUFFS - 50)) * (1 + 0.12)  # Uses Elixir of Iron instead


def sylas_shield():
    sylas_base = (800 + (2.16 * sylas_ap())) + (590 * 0.28)  # Moonstone + Redemption + Health Shard
    aery_base = 80 + (0.25 * sylas_ap())
    sylas_multiplier = 0.2 + 0.2 + 0.35  # Redemption + Mikaels + Moonstone Renewer
    return sylas_base * (1 + (SHIELD_MULTIPLIER + sylas_multiplier)) + (
            aery_base * (1 + (SHIELD_MULTIPLIER + sylas_multiplier)))


def shen_shield():
    shen_base = (800 + (2.16 * shen_ap())) + (590 * 0.28)  # Moonstone + Redemption + Health Shard
    aery_base = 80 + (0.25 * shen_ap())
    shen_multiplier = 0.1 + 0.2 + 0.2 + 0.35  # Ardent Censer + Redemption + Mikael's Blessing + Moonstone Renewer
    return shen_base * (1 + (SHIELD_MULTIPLIER + shen_multiplier)) + (
            aery_base * (1 + (SHIELD_MULTIPLIER + shen_multiplier)))


def lulu_shield():
    lulu_base = (240 + (0.4 * lulu_ap()))
    aery_base = 80 + (0.25 * lulu_ap())
    lulu_multiplier = 0
    return lulu_base * (1 + (SHIELD_MULTIPLIER + lulu_multiplier - 0.15)) + (
            aery_base * (1 + (SHIELD_MULTIPLIER + lulu_multiplier - 0.15)))


def lux_shield():
    lux_base = (125 + (0.35 * lux_ap()))
    # No Aery because Viego procs it instead
    lux_multiplier = 0.2 + 0.2  # Redemption + Mikaels
    return lux_base * (1 + SHIELD_MULTIPLIER + lux_multiplier)


def ivern_shield():
    ivern_base = (220 + (0.8 * ivern_ap()))
    # No Aery because Viego procs it instead
    ivern_multiplier = 0.2 + 0.2  # Mikaels + Redemption
    return ivern_base * (1 + SHIELD_MULTIPLIER + ivern_multiplier)


def lee_sin_shield():
    lee_sin_base = (275 + (0.8 * lee_sin_ap()))
    # No Aery because Viego procs it instead
    lee_sin_multiplier = 0.1 + 0.2 + 0.2  # Ardent Censer + Mikaels + Redemption
    return lee_sin_base * (1 + SHIELD_MULTIPLIER + lee_sin_multiplier)


def rakan_shield():
    rakan_base = (140 + (0.8 * rakan_ap()))
    # No Aery because Viego procs it instead
    rakan_multiplier = 0.2 + 0.2  # Mikaels + Redemption
    return rakan_base * (1 + SHIELD_MULTIPLIER + rakan_multiplier)


def viego_shield():
    viego_multiplier = 0.35
    aery_base = 80 + (0.25 + lux_ap())  # Aery will only proc once for final number. Don't know who it will proc on yet
    return ((lux_shield() * (1 + viego_multiplier)) * 2) \
           + (ivern_shield() * (1 + viego_multiplier)) \
           + (lee_sin_shield() * (1 + viego_multiplier)) \
           + (aery_base * (1 + viego_multiplier))\
           + (rakan_shield() * (1 + viego_multiplier))


def tahm_kench_shield():
    tahm_kench_base = tahm_kench_health() * 3
    guardian_proc_damage = 251
    guardian_base = (150 + (0.15 * tahm_kench_ap()) + (0.09 * (tahm_kench_health() - 2185)) - guardian_proc_damage)
    barrier = 455
    gargoyle_stoneplate = (tahm_kench_health() - 2185)
    steraks_gage = (100 + (0.4 * tahm_kench_health())) - guardian_proc_damage
    tahm_kench_multiplier = 0.35 + 0.2  # Moonstone Renewer + Redemption
    return (tahm_kench_base * (1 + tahm_kench_multiplier + SELF_SHIELD_MULTIPLIER)) \
           + (guardian_base * (1 + tahm_kench_multiplier + SELF_SHIELD_MULTIPLIER)) \
           + (barrier * (1 + tahm_kench_multiplier + SELF_SHIELD_MULTIPLIER)) \
           + (gargoyle_stoneplate * (1 + tahm_kench_multiplier + SELF_SHIELD_MULTIPLIER)) \
           + (steraks_gage * (1 + tahm_kench_multiplier + SELF_SHIELD_MULTIPLIER))


def total_shield():
    return round((sylas_shield() + shen_shield() + lulu_shield() + viego_shield() + tahm_kench_shield()))


def main():
    print("Sylas Total AP: " + str(sylas_ap()))
    print("Sylas Total Shielding: " + str(sylas_shield()))
    print("Shen Total AP: " + str(shen_ap()))
    print("Shen Total Shielding: " + str(shen_shield()))
    print("Lulu Total AP: " + str(lulu_ap()))
    print("Lulu Total Shielding: " + str(lulu_shield()))
    print("Lux Total AP: " + str(lux_ap()))
    print("Lux Total Shielding: " + str(lux_shield() * 2))
    print("Ivern Total AP: "+ str(ivern_ap()))
    print("Ivern Total Shielding: " + str(ivern_shield()))
    print("Lee Sin Total AP: " + str(lee_sin_ap()))
    print("Lee Sin Total Shielding: " + str(lee_sin_shield()))
    print("Rakan Total AP: " + str(rakan_ap()))
    print("Rakan Total Shielding: " + str(rakan_shield()))
    print("Viego Total Shielding: " + str(viego_shield()))
    print("Tahm Kench Total AP: " + str(tahm_kench_ap()))
    print("Tahm Kench Total Health: " + str(tahm_kench_health()))
    print("Tahm Kench Total Shielding: " + str(tahm_kench_shield()))
    print("Total Shielding: " + str(total_shield()))



if __name__ == "__main__":
    main()
