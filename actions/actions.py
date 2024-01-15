# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


from typing import Any, Text, Dict, List, Optional

#import arrow 
#import dateparser
from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict

#Slots to collect information to later use in action description exercises
#ALLOWED_INTENSITY_SIZES = ["beginner", "intermediate", "expert", "b", "i", "e"]
#ALLOWED_BODY_PART_TYPES = ["abdominals", "abductors", "adductors", "biceps", "calves","chest","forearms","glutes","hamstrings","lats","lower back","middle back","neck",
#                           "quadriceps","shoulders","traps","triceps"]


#class ValidateSimpleGymRoutineForm(FormValidationAction):
#    def name(self) -> Text:
#        return "validate_simple_gym_routine_form"
    
#    def validate_body_part( #validate_<slot_name>
#        self,
#        slot_value: Any,
#        dispatcher: CollectingDispatcher,
#        tracker: Tracker,
#        domain: DomainDict,
#    ) -> Dict[Text, Any]:
#        """Validate `body_part` value."""

#        if slot_value.lower() not in ALLOWED_BODY_PART_TYPES:
#            dispatcher.utter_message(text=f"We only accept body part exercises: {'/'.join(ALLOWED_BODY_PART_TYPES)}.")
#            return {"body_part": None}
#        dispatcher.utter_message(text=f"OK! You want to exercise {slot_value}.")
#        return {"body_part": slot_value}
    
#    def validate_level_intensity( #validate_<slot_name>
#        self,
#        slot_value: Any,
#        dispatcher: CollectingDispatcher,
#        tracker: Tracker,
#        domain: DomainDict,
#    ) -> Dict[Text, Any]:
#        """Validate `level_intensity` value."""

#        if slot_value not in ALLOWED_INTENSITY_SIZES:
#            dispatcher.utter_message(text=f"I don't recognize that level of intensity: b/i/e.")
#            return {"level_intensity": None}
#        dispatcher.utter_message(text=f"OK! You want a {slot_value} level of intensity.")
#        return {"level_intensity": slot_value}
    
#    def validate_number_of_exercises(
#        self,
#        slot_value: Any,
#        dispatcher: CollectingDispatcher,
#        tracker: Tracker,
#        domain: DomainDict,
#    ) -> Dict[Text, Any]:
#        """Validate `number_of_exercises` value."""
        
#        if not isinstance(slot_value, (int, str)):
#            dispatcher.utter_message(text="Please provide a valid number for the exercises.")
#            return {"number_of_exercises": None}
        
#        dispatcher.utter_message(text=f"OK! You want {slot_value} exercises.")
#        return {"number_of_exercises": slot_value}
    
#    def validate_description_exercises(
#        self,
#        slot_value: Any,
#        dispatcher: CollectingDispatcher,
#        tracker: Tracker,
#        domain: DomainDict,
#    ) -> Dict[Text, Any]:
#        """Validate `description_exercises` value."""
        
#        if not isinstance(slot_value, (str)):
#            dispatcher.utter_message(text="Please provide a valid response: yes/ok/perfect.")
#            return {"description_exercises": None}
        
#        dispatcher.utter_message(text=f"Perfect. I'll give you a description of exercises.")
#        return {"description_exercises": slot_value}

################################################################################################################################################
################################################################################################################################################
################################################################################################################################################  
#Advanced button slot validation for exercises

#SlotSet("body_part", None),
#SlotSet("level_intensity", None),
#SlotSet("number_of_exercises", None),
#SlotSet("description_exercises", None),
#SlotSet("requested_slot", None),

BODY_PART_TYPES = ["abdominals", "abductors", "adductors", "biceps", "calves","chest","forearms","glutes","hamstrings","lats","lower back","middle back","neck",
                           "quadriceps","shoulders","traps","triceps"]
INTENSITY_SIZES = ["beginner", "intermediate", "expert"]
NUMBER_EXERCISES = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

class AskForBodyPart(Action):
    def name(self) -> Text:
        return "action_ask_body_part"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: DomainDict
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text="Let's customize your gym routine. Please select body part from the options below:",
            buttons=[
                {"title": body_part, "payload": f"/inform{{\"body_part\":\"{body_part}\"}}"} for body_part in BODY_PART_TYPES
            ],
        )
        return []
class AskForLevelIntensity(Action):
    def name(self) -> Text:
        return "action_ask_level_intensity"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: DomainDict
    ) -> List[Dict[Text, Any]]:
        if tracker.get_slot("body_part"):
            dispatcher.utter_message(
                text="Please select level of intensity from the options below:",
                buttons=[
                    {"title": level, "payload": f"/inform{{\"level_intensity\":\"{level}\"}}"} for level in INTENSITY_SIZES
                ],
            )
        return []
    
class AskForNumberExercises(Action):
    def name(self) -> Text:
        return "action_ask_number_of_exercises"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: DomainDict
    ) -> List[Dict[Text, Any]]:
        if tracker.get_slot("level_intensity"):
            dispatcher.utter_message(
                text="Please select the number of exercises to perform from the options below:",
                buttons=[
                    {"title": num_exercises, "payload": f"/inform{{\"number_of_exercises\":\"{num_exercises}\"}}"} for num_exercises in NUMBER_EXERCISES
                ],
            )
        return []
           
class ValidateAdvancedGymRoutineForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_advanced_gym_routine_form"
    
    def validate_body_part( 
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `body_part` value."""

        if slot_value.lower() not in BODY_PART_TYPES:
            dispatcher.utter_message(text=f"We only accept body part exercises: {'/'.join(BODY_PART_TYPES)}.")
            return {"body_part": None}
        dispatcher.utter_message(text=f"OK! You want to exercise {slot_value}.")
        return {"body_part": slot_value}
    
    def validate_level_intensity( 
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `level_intensity` value."""

        if slot_value not in INTENSITY_SIZES:
            dispatcher.utter_message(text=f"I don't recognize that level of intensity: beginner/intermediate/expert.")
            return {"level_intensity": None}
        dispatcher.utter_message(text=f"OK! You want a {slot_value} level of intensity.")
        return {"level_intensity": slot_value}
    
    def validate_number_of_exercises(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `number_of_exercises` value."""
        if slot_value not in NUMBER_EXERCISES:
            dispatcher.utter_message(text="Please provide a valid number between 1-10 for the exercises.")
            return {"number_of_exercises": None}
        dispatcher.utter_message(text=f"OK! You want {slot_value} exercises.")
        return {"number_of_exercises": slot_value}
    
       
    def validate_description_exercises(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `description_exercises` value."""
        if not isinstance(slot_value, str):
            dispatcher.utter_message(text="Please provide a valid response: yes/ok/perfect.")
            return {"description_exercises": None}
        dispatcher.utter_message(text=f"Perfect. I'll give you a description of exercises.")
        return {"description_exercises": slot_value}
    
    def request_next_slot(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Optional[List[Dict[Text, Any]]]:
        """Request the next slot and utter template if needed, else return None"""

        for slot in self.required_slots(tracker):
            if self._should_request_slot(tracker, slot):
                # Check which slot is being requested and trigger the corresponding action
                if slot == 'body_part':
                    return self.deactivate()

                elif slot == 'level_intensity':
                    return self.deactivate()

                elif slot == 'number_of_exercises':
                    return self.deactivate()

                elif slot == 'description_exercises':
                    if self._should_request_slot(tracker, slot):
                        dispatcher.utter_message(template=f"utter_ask_{slot}", **tracker.slots)
                    return [SlotSet(slot)]
                    #return [SlotSet(REQUESTED_SLOT, slot)]

        return None
            
################################################################################################################################################
################################################################################################################################################
################################################################################################################################################        

#Action return exercises description
import csv 
import traceback

#def fetch_exercise_data(file_path="path/to/your/exercise_data.csv"):
def fetch_exercise_data(file_path="C:/Users/enman/OneDrive/Documents/Fordham University/Fall 2023/Natural Language Processing/Final Project/Gym exercise dataset/kagglegymfinal.csv"):    
    exercise_data = []
    with open(file_path, newline="", encoding='ISO-8859-1') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            exercise_data.append(row)
    return exercise_data

class Exercise:
    def __init__(self, title, instructions, rating, Equipment):
        self.title = title
        self.instructions = instructions
        self.rating = rating
        self.Equipment=Equipment

import ast
def format_exercise(exercise):
    try:
        instructions_list = ast.literal_eval(exercise.instructions)
        if isinstance(instructions_list, list):
            formatted_instructions = "\n".join([f"{i + 1}. {step}" for i, step in enumerate(instructions_list)])
        else:
            formatted_instructions = "Invalid instructions format"
    except (ValueError, SyntaxError):
        formatted_instructions = "Invalid instructions format"
    return f"{exercise.title} with {exercise.Equipment} equipment:\n{formatted_instructions}"

class ActionExerciseDescription(Action):
    def name(self) -> Text:
        return "action_exercise_description"
    

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        try:
            exercise_data = fetch_exercise_data()

            # Get user input
            number_of_exercises = tracker.get_slot("number_of_exercises")
            level_intensity = tracker.get_slot("level_intensity")
            body_part = tracker.get_slot("body_part")

            #convert number of exercises to an integer
            number_of_exercises = int(number_of_exercises)

            # Filter exercises based on user input
            filtered_exercises = [
                #exercise
                Exercise(exercise["Title"], exercise["instructions"],exercise["Rating"],exercise["Equipment"])
                for exercise in exercise_data
                if (
                    exercise["Level"].lower() == level_intensity.lower()
                    and exercise["muscle_gp"].lower() == body_part.lower()
                )
            ]

            # Sort exercises by Rating in descending order
            sorted_exercises = sorted(filtered_exercises, key=lambda x: x.rating, reverse=True)


            # Get the top N exercises
            top_n_exercises = sorted_exercises[:number_of_exercises]

            # Return exercise descriptions
            for exercise in top_n_exercises:

                formatted_exercise_text = format_exercise(exercise)
                dispatcher.utter_message(text=formatted_exercise_text)
                
              
            return [
            SlotSet("body_part", None),
            SlotSet("level_intensity", None),
            SlotSet("number_of_exercises", None),
            SlotSet("description_exercises", None),
            SlotSet("requested_slot", None),
        ]
        
        except Exception as e:
        # Print the exception and traceback for debugging        
            traceback.print_exc()
            dispatcher.utter_message(f"An error occurred: {str(e)}")
        # You can also return an error event if needed
            return [Exception(self.name(), str(e))]
################################################################################################################################################
################################################################################################################################################
################################################################################################################################################        

#Image exercise action
import pandas 

class ActionImageExercise(Action):

    def name(self) -> Text:
        return "action_image_exercise"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        #print("Tracker content:", tracker)
        
        # Get exercise names from the slot
        if 'entities' in tracker.latest_message:
            exercise_entities = tracker.latest_message['entities']
            #print("Entities:", exercise_entities)

            exercise_names = [entity['value'].lower() for entity in exercise_entities if entity['entity'] == 'exercise_lookup']
            #print("Exercise Names:", exercise_names)

            exercise_data = pandas.DataFrame(fetch_exercise_data())

            # Filter the dataset based on the provided exercise names
            filtered_exercises = exercise_data[exercise_data['Exercise_Name'].str.lower().isin(exercise_names)]

            

            if filtered_exercises.empty:
                dispatcher.utter_message(text=f"Sorry, I didn't recognize this exercise. Is it spelled correctly?")
            else:
                # Create a message with exercise_name: image_url pairs
                exercise_messages = [
                    f"{exercise['Exercise_Name']}: {exercise['Exercise_Image']}"
                    for _, exercise in filtered_exercises.iterrows()
                ]

                # Sending the exercise_name: image_url pairs to the user
                for exercise_message in exercise_messages:
                    dispatcher.utter_message(text=exercise_message)
        
        else:
            dispatcher.utter_message(text="No entities found in the tracker.")


        return []

################################################################################################################################################
################################################################################################################################################
################################################################################################################################################   
    
#Recipe actions: details of a recipe, calories, protein, total time, carbohydrates, fat
def fetch_recipe_data(file_path="C:/Users/enman/OneDrive/Documents/Fordham University/Fall 2023/Natural Language Processing/Final Project/recipedataset.csv"):    
    recipe_data = []
    with open(file_path, newline="", encoding='ISO-8859-1') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            recipe_data.append(row)
    return recipe_data

class Recipe:
    def __init__(self, name, description, recipeIngredient, directions,totalTime,image,calories,carbohydrates,protein,fat):
        self.name = name
        self.description = description
        self.recipeIngredient = recipeIngredient
        self.directions=directions
        self.totalTime=totalTime
        self.image=image
        self.calories=calories
        self.carbohydrates=carbohydrates
        self.protein=protein
        self.fat=fat

class Actioncalories(Action):

    def name(self) -> Text:
        return "action_calories"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        
        # Get calories from the recipe name
        if 'entities' in tracker.latest_message:
            recipe_entities = tracker.latest_message['entities']

            recipe_names = [entity['value'].lower() for entity in recipe_entities if entity['entity'] == 'recipe_name']

            recipe_data = pandas.DataFrame(fetch_recipe_data())

            filtered_recipe = recipe_data[recipe_data['name'].str.lower().isin(recipe_names)]


            if filtered_recipe.empty:
                dispatcher.utter_message(text=f"Sorry, I didn't recognize the recipe information provided. Is it spelled correctly?")
            else:
                calorie_messages = [
                    f"Recipe {calorie['name']} has {calorie['calories']} calories"
                    for _, calorie in filtered_recipe.iterrows()
                ]

                for calorie_message in calorie_messages:
                    dispatcher.utter_message(text=calorie_message)
        
        else:
            dispatcher.utter_message(text="No entities found in the tracker.")


        return []

class Actionprotein(Action):

    def name(self) -> Text:
        return "action_protein"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
                
        if 'entities' in tracker.latest_message:
            recipe_entities = tracker.latest_message['entities']

            recipe_names = [entity['value'].lower() for entity in recipe_entities if entity['entity'] == 'recipe_name']

            recipe_data = pandas.DataFrame(fetch_recipe_data())

            filtered_recipe = recipe_data[recipe_data['name'].str.lower().isin(recipe_names)]


            if filtered_recipe.empty:
                dispatcher.utter_message(text=f"Sorry, I didn't recognize the recipe information provided. Is it spelled correctly?")
            else:
                protein_messages = [
                    f"Recipe {protein['name']} has {protein['protein']} grams of protein"
                    for _, protein in filtered_recipe.iterrows()
                ]

                for protein_message in protein_messages:
                    dispatcher.utter_message(text=protein_message)
        
        else:
            dispatcher.utter_message(text="No entities found in the tracker.")


        return []

class Actiontotaltime(Action):

    def name(self) -> Text:
        return "action_total_time"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
                
        if 'entities' in tracker.latest_message:
            recipe_entities = tracker.latest_message['entities']

            recipe_names = [entity['value'].lower() for entity in recipe_entities if entity['entity'] == 'recipe_name']

            recipe_data = pandas.DataFrame(fetch_recipe_data())

            filtered_recipe = recipe_data[recipe_data['name'].str.lower().isin(recipe_names)]


            if filtered_recipe.empty:
                dispatcher.utter_message(text=f"Sorry, I didn't recognize the recipe information provided. Is it spelled correctly?")
            else:
                total_time_messages = [
                    f"Recipe {total_time['name']} needs a total of {total_time['totalTime']} minutes"
                    for _, total_time in filtered_recipe.iterrows()
                ]

                for total_time_message in total_time_messages:
                    dispatcher.utter_message(text=total_time_message)
        
        else:
            dispatcher.utter_message(text="No entities found in the tracker.")


        return []

class Actioncarbohydrates(Action):

    def name(self) -> Text:
        return "action_carbohydrates"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
                
        if 'entities' in tracker.latest_message:
            recipe_entities = tracker.latest_message['entities']

            recipe_names = [entity['value'].lower() for entity in recipe_entities if entity['entity'] == 'recipe_name']

            recipe_data = pandas.DataFrame(fetch_recipe_data())

            filtered_recipe = recipe_data[recipe_data['name'].str.lower().isin(recipe_names)]


            if filtered_recipe.empty:
                dispatcher.utter_message(text=f"Sorry, I didn't recognize the recipe information provided. Is it spelled correctly?")
            else:
                carbohydrates_messages = [
                    f"Recipe {carbohydrates['name']} has a total of {carbohydrates['carbohydrates']} carbohydrates"
                    for _, carbohydrates in filtered_recipe.iterrows()
                ]

                for carbohydrates_message in carbohydrates_messages:
                    dispatcher.utter_message(text=carbohydrates_message)
        
        else:
            dispatcher.utter_message(text="No entities found in the tracker.")


        return []

class Actionfat(Action):

    def name(self) -> Text:
        return "action_fat"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
                
        if 'entities' in tracker.latest_message:
            recipe_entities = tracker.latest_message['entities']

            recipe_names = [entity['value'].lower() for entity in recipe_entities if entity['entity'] == 'recipe_name']

            recipe_data = pandas.DataFrame(fetch_recipe_data())

            filtered_recipe = recipe_data[recipe_data['name'].str.lower().isin(recipe_names)]


            if filtered_recipe.empty:
                dispatcher.utter_message(text=f"Sorry, I didn't recognize the recipe information provided. Is it spelled correctly?")
            else:
                fat_messages = [
                    f"Recipe {fat['name']} has {fat['fat']} grams of fat"
                    for _, fat in filtered_recipe.iterrows()
                ]

                for fat_message in fat_messages:
                    dispatcher.utter_message(text=fat_message)
        
        else:
            dispatcher.utter_message(text="No entities found in the tracker.")


        return []
    

class Actionrecipeinfo(Action):

    def name(self) -> Text:
        return "action_recipe_info"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
                
        if 'entities' in tracker.latest_message:
            recipe_entities = tracker.latest_message['entities']

            recipe_names = [entity['value'].lower() for entity in recipe_entities if entity['entity'] == 'recipe_name']

            recipe_data = pandas.DataFrame(fetch_recipe_data())

            filtered_recipe = recipe_data[recipe_data['name'].str.lower().isin(recipe_names)]

            if not filtered_recipe.empty:
                # Extracting values from the DataFrame
                name = filtered_recipe['name'].values[0]
                image = filtered_recipe['image'].values[0]
                description = filtered_recipe['description'].values[0]
                calories = filtered_recipe['calories'].values[0]
                carbs = filtered_recipe['carbohydrates'].values[0]
                protein = filtered_recipe['protein'].values[0]
                fat = filtered_recipe['fat'].values[0]
                total_time = filtered_recipe['totalTime'].values[0]
                ingredients = filtered_recipe['recipeIngredient'].values[0]
                directions = filtered_recipe['directions'].values[0]

                # Constructing the response
                response = f"{name}\n{image}\nDescription of recipe: {description}\nCalories: {calories}, Carbs: {carbs} grams, Protein: {protein} grams, Fat: {fat} grams\nTotal Time: {total_time} minutes\n"

                # Ingredients
                response += "Ingredients:\n"
                for ingredient in ast.literal_eval(ingredients):
                    response += f"- {ingredient}\n"

                # Directions
                response += "Directions:\n"
                for i, direction in enumerate(ast.literal_eval(directions), start=1):
                    response += f"{i}. {direction}\n"

                dispatcher.utter_message(text=response)

            else:
                dispatcher.utter_message(text=f"Recipe information not found.")
        else:
            dispatcher.utter_message(text=f"Recipe information not found.")

        return []
    
################################################################################################################################################
################################################################################################################################################
################################################################################################################################################  
#Recipe action: Multiple ways of asking for a recipe: total time, calories, carbohydrates, protein, fat and any word in the name of the recipe

import re 

def extract_number_with_unit(text):
    match = re.search(r'(\d+)\s*([a-zA-Z]+)?', text)
    
    if match:
        number = int(match.group(1))
        unit = match.group(2)
        return number, unit
    else:
        return None, None

def find_recipe_by_name(name, recipe_data):
    # Perform a 'like' search on the 'name' column
    matching_recipes = recipe_data[recipe_data['name'].str.contains(name, case=False, regex=True)]
    
    if matching_recipes.empty:
        return None
    else:
        # Randomly select one recipe from the matching ones
        selected_recipe = matching_recipes.sample(n=1)
        return selected_recipe
    
class Actionmultiplerecipeinfo(Action):

    def name(self) -> Text:
        return "action_multiple_recipe_info"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
                
        if 'entities' in tracker.latest_message:
            entities = tracker.latest_message['entities']
            entity_column_mapping = {
                'calories': 'calories',
                'protein': 'protein',
                'total_time': 'totalTime',
                'carbohydrates': 'carbohydrates',
                'fat': 'fat',
                'recipe_name': 'name'
                #'ingredients_recipe': 'name'
            }

            # Extract the names of entities and their corresponding columns
            entity_column_pairs = []

            for i in range(len(entities)):
                entity = entities[i]

                if entity['entity'] == 'number_recipe':
                    # Ensure it's not the last entity
                    if i + 1 < len(entities):
                        next_entity = entities[i + 1]
                        entity_column_pairs.append((entity['value'], entity_column_mapping.get(next_entity['entity'])))
                else:
                    entity_column_pairs.append((entity.get('value', ''), entity_column_mapping.get(entity['entity'])))
            #print("First entity column pairs:",entity_column_pairs)
            # Remove pairs with None values (entities without corresponding columns)
            entity_column_pairs = [(name, column) for name, column in entity_column_pairs if column is not None]
            #print("Second entity column pairs:",entity_column_pairs)
            #recipe_data = fetch_recipe_data()
            recipe_data = pandas.DataFrame(fetch_recipe_data())

            # Initialize an empty DataFrame to store filtered results
            filtered_recipe = pandas.DataFrame()

            # If there are entities to filter by
            if entity_column_pairs:
                not_found_values = []
                for name, column in entity_column_pairs:
                    # Special case for 'ingredients_recipe'
                    if column == 'name':
                        matching_recipe = find_recipe_by_name(name, recipe_data)
                    else:
                        # Filter the DataFrame based on the current entity and column
                        matching_recipe = recipe_data[recipe_data[column].astype(str).str.contains(name, case=False, regex=True)]
                    
                    # Append the matching recipe to the filtered results
                    filtered_recipe = pandas.concat([filtered_recipe, matching_recipe], ignore_index=True)

                    # Check if the value was not found
                    if matching_recipe.empty:
                        not_found_values.append(name)

                # Drop duplicate rows from the filtered results
                filtered_recipe = filtered_recipe.drop_duplicates()

                if not filtered_recipe.empty:
                    # Randomly select one recipe from the filtered results
                    selected_recipe = filtered_recipe.sample(n=1)
                    #print("selected recipe values:",selected_recipe)

                    # Extracting values from the DataFrame
                    name = selected_recipe['name'].values[0]
                    image = selected_recipe['image'].values[0]
                    description = selected_recipe['description'].values[0]
                    calories = selected_recipe['calories'].values[0]
                    carbs = selected_recipe['carbohydrates'].values[0]
                    protein = selected_recipe['protein'].values[0]
                    fat = selected_recipe['fat'].values[0]
                    total_time = selected_recipe['totalTime'].values[0]
                    
                    ingredients = selected_recipe['recipeIngredient'].values[0]
                    directions = selected_recipe['directions'].values[0]

                    # Constructing the response
                    response = f"{name}\n{image}\nDescription of recipe: {description}\nCalories: {calories}, Carbs: {carbs} grams, Protein: {protein} grams, Fat: {fat} grams\nTotal Time: {total_time} minutes\n"

                    # Ingredients
                    response += "Ingredients:\n"
                    for ingredient in ast.literal_eval(ingredients):
                        response += f"- {ingredient}\n"

                    # Directions
                    response += "Directions:\n"
                    for i, direction in enumerate(ast.literal_eval(directions), start=1):
                        response += f"{i}. {direction}\n"

                    dispatcher.utter_message(text=response)

                else:
                    not_found_message = f"Values {', '.join(not_found_values)} not found in the available options."
                    dispatcher.utter_message(text=not_found_message)

            else:
                dispatcher.utter_message(text="No valid entities found in the tracker.")

        else:
            dispatcher.utter_message(text="No entities found in the tracker.")

        return []
    