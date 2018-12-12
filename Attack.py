class Attack:
  def __init__(	
	  	self, 
		valid_url, 
		target_url, 
		has_payload,
		is_blind_injection,
		specified_attack
	):
    self.valid_url = valid_url
    self.target_url = target_url
    self.has_payload = has_payload
    self.is_blind_injection = is_blind_injection
    self.specified_attack = specified_attack