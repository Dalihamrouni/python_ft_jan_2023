/* 
  Given an array of objects / dictionaries to represent new inventory,
  and an array of objects / dictionaries to represent current inventory,
  update the quantities of the current inventory
  
  if the item doesn't exist in current inventory, add it to the inventory
  return the current inventory after updating it.
*/

var newInv1 = [
    { name: "Grain of Rice", quantity: 9000 },
    { name: "Peanut Butter", quantity: 50 },
    { name: "Royal Jelly", quantity: 20 },
  ];
  var currInv1 = [
    { name: "Peanut Butter", quantity: 20 },
    { name: "Grain of Rice", quantity: 1 },
  ];
  var expected1 = [
    { name: "Peanut Butter", quantity: 70 },
    { name: "Grain of Rice", quantity: 9001 },
    { name: "Royal Jelly", quantity: 20 },
  ];
  
  var newInv2 = [];
  var currInv2 = [{ name: "Peanut Butter", quantity: 20 }];
  var expected2 = [{ name: "Peanut Butter", quantity: 20 }];
  
  var newInv3 = [{ name: "Peanut Butter", quantity: 20 }];
  var currInv3 = [];
  var expected3 = [{ name: "Peanut Butter", quantity: 20 }];
  
  /**
   * @typedef {Object} Inventory
   * @property {string} Inventory.name The name of the item.
   * @property {number} Inventory.quantity The quantity of the item.
   */
  
  /**
   * Updates the current inventory based on the new inventory.
   * @param {Array<Inventory>} newInv A shipment of new inventory.
   *    An array of inventory objects.
   * @param {Array<Inventory>} currInv
   * @return The currInv after being updated.
   */
//   function updateInventory(newInv, currInv) {

//     for (var i =0 ;i<newInv.length; i++){
//         var itemFound = false;

//     }
//   }
  
  /*****************************************************************************/