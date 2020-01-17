observations_to_birds_list = {}
for bird, observations in bird_to_observations.items():
  if observations in observations_to_birds_list:
    observations_to_birds_list[observations].append(bird)
  else:
    observations_to_birds_list[observations] = [bird]
    
 observations_to_birds_list
{1:['nother fulmar', 'snow goose'], 2:['long-tailed jaeger'], 5:['canada goose']}
