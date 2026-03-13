SELECT  c.code_insee_com, c.nom_com, cl.RR_med,NBJRR5_med,cl.NBJRR1_med,cl.NBJRR10_med,cl.Tmin_med,cl.Tmax_med,cl.Tens_vap_med,cl.Force_vent_med,
cl.Insolation_med,cl.Rayonnement_med,se.niveau_vie_median_2021
FROM UE403_COMMUNES  c
JOIN UE403_GEO_CLIMATIQUES  cl 
    ON c.code_insee_com = cl.code_insee_com
JOIN UE403_SOCIO_ECONOMIQUES  se 
    ON c.code_insee_com = se.code_insee_com;

    