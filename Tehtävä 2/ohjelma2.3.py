#tehtävä 2.3
kantastr = input("anna suorakulmion kanta:")
kanta = float(kantastr)
korkeusstr = input("anna suorakulmion korkeus:")
korkeus = float(korkeusstr)
skulmio_pinta_ala = (kanta * korkeus)
skulmio_piiri = (2 * kanta + 2 * korkeus)
print("suorakulmion pinta ala on:" + str(skulmio_pinta_ala) + ". " "suorakulmion piiri on:" + str(skulmio_piiri))
