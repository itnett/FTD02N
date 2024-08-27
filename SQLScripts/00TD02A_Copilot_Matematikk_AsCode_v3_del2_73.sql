sql
SELECT mass, latent_heat, 
       mass * latent_heat AS heat_required 
FROM PhaseTransitions;