using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace LinearMachineLearning.DataHandling
{
    public class DataSet
    {
        #region Parameters
        public int InputSize { get; set; }
        public List<DataPoint> Examples { get; set; }
        public int NumberExamples { get; set; } 
        #endregion

        #region Constructors
        public DataSet()
        {
            InputSize = 1;
            Examples = new List<DataPoint>();
            NumberExamples = 0;
        }
        public DataSet(string filePath)
        {
            Examples = new List<DataPoint>();
            string[] lines = System.IO.File.ReadAllLines(filePath);
            string[] counting = lines[0].Split(',');
            InputSize = counting.Length;
            NumberExamples = lines.Length;
            for(int exampleNumber = 0; exampleNumber < lines.Length; exampleNumber++)
            {
                double[] futureInput = new double[InputSize];
                double output = 0;
                futureInput[0] = 1;
                string[] vals = lines[exampleNumber].Split(',');
                output = Convert.ToDouble(vals[vals.Length - 1]);
                for(int indexFromLine = 0; indexFromLine < vals.Length - 1; indexFromLine++)
                {
                    futureInput[indexFromLine + 1] = Convert.ToDouble(vals[indexFromLine]);
                }
                Examples.Add(new DataPoint(futureInput, output));
            }
        }
        #endregion

        #region Methods
        #endregion
    }
}
