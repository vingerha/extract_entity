# SETUP VARIABLES FROM HASS CALL
entity_in = data.get('entity')
attributes = data.get('attributes')
save_file = data.get('save_file')

# SET YAML RECEIVER VARIABLE
text = ""

# PROCESS ENTITY
logger.warning('Process entity')
# GET ENTITY DATA FROM HASS
entity = ("%r" % entity_in).strip("'")
logger.warning("Entity: %s", entity)

status = hass.states.get(entity)

# ENTITY STATE
text = text + "{ 'entity': '" + entity + "'," + "\n"
text = text + "'state': '" + status.state + "'," + "\n"

# ENTITY ATTRIBUTES

logger.debug("Getting attributes: %s",attributes)
for i in attributes:

    # GET ATTRIBUTE BY JSON ARRAY PASSED BY HASS CALL
    attributeState = ("%r" % i).strip("'")
    # DISPLAY ATTRIBUTE IF NOT EMPTY
    if status.attributes.get(attributeState):
        text = text + "  '" + attributeState + "': " + str(status.attributes.get(attributeState)) + "\n"

text = text + "}" + "\n" + "\n"
        

if save_file:
    # SAVE SCENE CONFIGURATION TO FILE
    hass.services.call("notify", "json_file_generator", {"message": "{}".format(text).replace('\'', '\"')})
else:
    # OUTPUT FORMATTED YAML TO LOG FILE
    logger.debug(text)
    